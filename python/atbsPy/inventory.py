inventory = {"rope": 1, "dagger": 1, "torch": 6, "gold coin": 1, "arrow": 12}
dragonLoot = ["rope", "gold coin", "gold coin", "ruby"]


def addToInventory(inventory, addedItem):
    for item in addedItem:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def outputInventory(inventory):
    print("inventory:")
    totalItems = 0
    for k, v in inventory.items():
        print(v, k)
        totalItems += v
    print("there are", totalItems, "in your inventory")


inventory = addToInventory(inventory, dragonLoot)
outputInventory(inventory)
