import pytest
# The following line imports the Vendor class from the module vendor inside the swap_meet package.
from swap_meet.vendor import Vendor

#### WAVE 1###
### test 1.1 PASSED ###
def test_vendor_has_inventory():
    vendor = Vendor()
    assert len(vendor.inventory) is 0

### test 1.2 PASSED ###
def test_vendor_takes_optional_inventory():
    inventory = ["a", "b", "c"]
    vendor = Vendor(inventory=inventory)
    assert len(vendor.inventory) is 3
    assert "a" in inventory
    assert "b" in inventory
    assert "c" in inventory

### test 1.3 PASSED ###
def test_adding_to_inventory():
    vendor = Vendor()
    item = "new item"

    result = vendor.add(item)

    assert len(vendor.inventory) is 1
    assert item in vendor.inventory
    assert result is item

### test 1.4 PASSED ###
def test_removing_from_inventory_returns_item():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c", item]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) is 3
    assert item not in vendor.inventory
    assert result is item

### test 1.5 PASSED ###
def test_removing_not_found_is_false():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c"]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) is 3
    assert result is False
