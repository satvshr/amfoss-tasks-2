import logging, random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s -%(message)s')
logging.debug("start of the program")
def convert(guess):
    if guess == 'heads':
        guess = 1
    else:
        guess = 0

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug("taking value of guess")
if guess == 'heads':
        guess = 1
else:
        guess = 0
print(guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
    logging.debug("matching toss value")

else:
    print('Nope! Guess again!')
    logging.debug("guessing again cuz value is wrong")
    guess = input()
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    logging.debug("New guess input")    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        print(toss)
        print(guess)
