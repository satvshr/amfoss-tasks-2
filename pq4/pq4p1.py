list = []
while True:
    print('Enter element ' + str(len(list) + 1) +' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    list += [name]
print('The list consists of:')
for i in list:
    if i == list[-1]:
        print(' and '+ i)
    elif i == list[-2]:
        print(i, end='') 
    else:
        print(i + ',', end='')