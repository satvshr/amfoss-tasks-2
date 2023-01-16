import pyinputplus as pyip
import random, time

q = 10
a = 0
for no in range(1, q+1):
    # Pick two random numbers:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    print('#%s: %s x %s = ' % (no, x, y))  
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        z = pyip.inputInt(allowRegexes=['%d'], timeout=8, limit=3)    
    except pyip.TimeoutException:
        print('Out of time!')
        continue
    except pyip.RetryLimitException:
        print('Out of tries!')
        continue
    if z == (x * y):
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        a += 1 
    else:
        print("Incorrect")
        print("The correct answer was %d" % (x*y))
    time.sleep(1) # Brief pause to let user see the result.
print('Score: %d / %d' % (a, q))