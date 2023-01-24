import pyinputplus as pyip
import random, time

q = 10
a = 0
for no in range(1, q+1):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    print('#%s: %s x %s = ' % (no, x, y))  
    try:
        z = pyip.inputInt(allowRegexes=['%d'], timeout=8, limit=3)    
    except pyip.TimeoutException:
        print('Out of time!')
        continue
    except pyip.RetryLimitException:
        print('Out of tries!')
        continue
    if z == (x * y):
        print('Correct!')
        a += 1 
    else:
        print("Incorrect")
        print("The correct answer was %d" % (x*y))
    time.sleep(1) 
print('Score: %d / %d' % (a, q))