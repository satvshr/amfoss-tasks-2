import random
sum = 0
for experimentNumber in range(10000):
    counter = 0
    coin = []
    for j in range(100):
        coin.append(random.randint(0,1))
    for i in range(len(coin)-5):
            if coin[i] == coin[i+1] == coin[i+2] == coin[i+3]== coin[i+4] == coin[i+5]:
                counter += 1
                #i+=6
    sum += counter
print("The average is: ", sum/10000)