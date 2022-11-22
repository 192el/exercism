"""Functions to keep track and alter inventory."""
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.
    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for i in range(len(items)):
        if items[i] not in inventory:
            inventory[f'{items[i]}'] = items.count(items[i])
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for i in range(len(items)):
        if items[i] in inventory:
            inventory[items[i]] = inventory[items[i]] + 1
        elif items[i] not in inventory:
            inventory[items[i]] = 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for i in range(len(items)):
        if items[i] in inventory:
            if inventory[items[i]] > 0:
                inventory[items[i]] = inventory[items[i]] - 1
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    pairs = []
    for x, y in inventory.items():
        if y > 0:
            pairs.append((x, y))
    return pairs
