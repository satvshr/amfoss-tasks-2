catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +'(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for i in catNames:
    if i == catNames[-1]:
        print(' and '+ i, end='') 
    else:
        print(i + ',', end='')