import pytest
from inventory_manager import find_matching_items, load_inventory, save_inventory


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
        #("", 0), # empty search term
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


