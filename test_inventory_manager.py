import pytest
from inventory_manager import find_matching_items, load_inventory, save_inventory, remove_item_by_number, update_item_quantity


@pytest.fixture
def sample_inventory():
    return [
        "Laptop Charger|Electronics|8",
        "Dry-Erase Markers|Classroom Supplies|4",
        "Pencils|Classroom Supplies|26",
        "USB Cable|Electronics|12"
    ]

def test_inventory_file(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert len(inventory) == 4

def test_missing_inventory_file(tmp_path):
    # Arrange
    test_file = tmp_path / "nonexistent.txt"
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert len(inventory) == 0

def test_blank_lines_are_ignored(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    sample_inventory.append("")  # Add a blank line
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert len(inventory) == 4

def test_quantities_converted_to_integers(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert isinstance(inventory[0]["quantity"], int)
    assert isinstance(inventory[1]["quantity"], int)

def test_correct_format(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert inventory[0]["name"] == "Laptop Charger"
    assert inventory[0]["category"] == "Electronics"
    assert inventory[0]["quantity"] == 8


def test_save_empty_inventory(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    # Act
    save_inventory([], str(test_file))
    # Assert
    assert test_file.read_text() == ""

def test_persistent_save_function(tmp_path, sample_inventory):
    # Arrange
    source_file = tmp_path / "source_inventory.txt"
    source_file.write_text("\n".join(sample_inventory))
    inventory = load_inventory(str(source_file))
    test_file = tmp_path / "inventory.txt"
    # Act
    save_inventory(inventory, str(test_file))
    # Assert
    assert test_file.read_text() == "\n".join(sample_inventory) + "\n"

def test_exact_item_search(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert inventory[0]["name"] == "Laptop Charger"
    assert inventory[0]["category"] == "Electronics"
    assert inventory[0]["quantity"] == 8

@pytest.mark.parametrize(
    ("search_term", "expected_count"),
    [
        ("laptop", 1),
        ("charger", 1),
        ("pencils", 1),
        ("cab", 1),
        ("electronics", 0), # no matching items
        ("er", 2), # multiple matching items appear
    ],
)
def test_partial_search(tmp_path, sample_inventory, search_term, expected_count):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert len(find_matching_items(inventory, search_term)) == expected_count

def test_search_ignores_capitalization(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    # Act
    inventory = load_inventory(str(test_file))
    # Assert
    assert len(find_matching_items(inventory, "LAPTOP")) == 1


@pytest.mark.parametrize(
    ("item_number", "expected_inventory_index"),
    [
        (0, None), # Invalid item number
        (-1, None), # Negative invalid item number
        (1, 0), # Remove the first item
        (2, 1), # Remove the second item
        (3, 2), # Remove the third item
        (4, 3), # Remove the last item
        (5, None), # Larger than inventory size
    ],
)
def test_remove_item(tmp_path, sample_inventory, item_number, expected_inventory_index):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    inventory = load_inventory(str(test_file))
    # Act
    removed_item = remove_item_by_number(inventory, item_number)
    # Assert
    if expected_inventory_index is None:
        assert removed_item is None
        assert len(inventory) == len(sample_inventory)
        return

    expected_name, expected_category, expected_quantity = sample_inventory[
        expected_inventory_index
    ].split("|")
    assert removed_item == {
        "name": expected_name,
        "category": expected_category,
        "quantity": int(expected_quantity),
    }

@pytest.mark.parametrize(
    ("new_quantity", "expected_updated", "expected_quantity"),
    [
        (0, True, 0), # Valid quantity
        (10, True, 10), # Valid quantity
        (-1, False, 4), # Negative quantity
        ("not a number", False, 4), # Invalid quantity
    ],
)
def test_update_quantity(
    tmp_path, sample_inventory, new_quantity, expected_updated, expected_quantity
):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("\n".join(sample_inventory))
    inventory = load_inventory(str(test_file))
    item_number = 2  # Update the second item
    # Act
    updated = update_item_quantity(inventory, item_number, new_quantity)
    # Assert
    assert updated is expected_updated
    assert inventory[item_number - 1] == {
        "name": "Dry-Erase Markers",
        "category": "Classroom Supplies",
        "quantity": expected_quantity,
    }

