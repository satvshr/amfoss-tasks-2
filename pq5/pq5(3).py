def addToInventory(inventory, addedItems):
    for i in list(inventory):
        for j in addedItems:
            if j in i:
                inventory[i] += 1
            if j not in i:
                


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)