
import time, pyperclip

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
clip = ''

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2))
        totalTime = str(round(time.time() - startTime, 2))
        strlap = str(lapNum)
        info = 'Lap #%s: %s (%s)' % (strlap.rjust(3), str(totalTime).center(6), lapTime.rjust(6))
#        print('Lap #', end = '')
#        l = len(strlap)
#        print(strlap.rjust(3-l)+':', end='')
#        l = len(totalTime)
#        print(totalTime.rjust(10-l), end='')
#        print('('.rjust(3), end ='')
#        l = len(lapTime)
#        print(lapTime.rjust(10-l), end='')
#        print(')')
        print(info)
        lapNum += 1
        clip += info
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    pyperclip.copy(clip)
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')