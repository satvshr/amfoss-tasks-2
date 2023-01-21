import re, os, shutil
dirlist = os.listdir('/home/satvshr/Desktop/amfoss-tasks-2/pq10/gapsfill')
total = 0
dir = []
newdir = []
for i in dirlist:
    total += 1
    dir.append(i)
dir.sort()
object = re.compile(r'00[0-total]')
for i in range(total): 
    if dir[i][-1] != i+1:
        a = str(dir[i])
        v = a.replace(dir[i][-1], str(i+1))
        print(a)
        print(v)
        shutil.move(os.path.join(('/home/satvshr/Desktop/amfoss-tasks-2/pq10/gapsfill', a)), (os.path.join('/home/satvshr/Desktop/amfoss-tasks-2/pq10/gapsfill', v)))
        newdir.append(v)
        #dir[i][-1] = i
print(newdir)

    
    




