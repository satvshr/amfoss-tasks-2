
import time

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2))
        totalTime = str(round(time.time() - startTime, 2))
        strlap = str(lapNum)
        print('Lap #', end = '')
        l = len(strlap)
        print(strlap.rjust(3-l)+':', end='')
        l = len(totalTime)
        print(totalTime.rjust(10-l), end='')
        print('('.rjust(3), end ='')
        l = len(lapTime)
        print(lapTime.rjust(10-l), end='')
        print(')')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')