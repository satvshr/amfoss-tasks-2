def collatz(number):
    if number % 2 == 0:
        print (number//2)
        return number//2
    if number % 2 == 1:
        print (3 * number + 1)
        return 3 * number + 1
try:
    n = int(input("Enter your number:"))
    while collatz(n) != 1:
        collatz(n)
        n = collatz(n)
except ValueError:
    print("Please enter an integer")


    