tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
lenlist=[]
table1={0:[], 1:[], 2:[], 3:[]}


for i in tableData:
    for j in range(len(i)):
        table1[j].append(i[j])
        print(table1)

for i,v in table1.items():
    a = ' '.join(v)
    lenlist.append(len(a))
print(lenlist)
x = max(lenlist)
for i in range(len(table1)):
    print(" " * (x - len(" ".join(table1[i]))) + " ".join(table1[i]))



