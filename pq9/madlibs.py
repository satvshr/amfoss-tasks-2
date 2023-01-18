string = "The ADJECTIVE panda walked to the NOUN and then VERB . A nearby NOUN was unaffected by these events ."
x = string.split()
print(x)
for i in range(len(x)):
    if x[i] == 'ADJECTIVE' or x[i] == 'NOUN' or x[i] == 'ADVERB' or x[i] == 'VERB':
        a = input(f"What word do you want to replace for {x[i]} ? ")
        x[i] = a
print(" ".join(x))