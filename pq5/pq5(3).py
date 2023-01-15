def addToInventory(inventory, addedItems):
    for j in addedItems:
            if j in inventory:
                inventory[j] += 1        
            if j not in inventory:
                inventory.setdefault(j, 1)
    return(inventory)
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print( str(v) + ' ' + k )
        item_total += v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)