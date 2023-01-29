import random, time, re

question = 10
answer = 0
for qno in range(question):
    attempts = 0

    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f"{qno + 1}: {num1} * {num2}\n"
    teacherRegex = re.compile(f'^{num1 * num2}$')
    start = int(time.time())
    #print(int(time.time()))
    print(prompt)
    answer = input()
    while attempts < 3:
        end = int(time.time())
        #print(int(time.time()))
        elapsedTime = end - start
        if elapsedTime > 8:
            print("Out of time!")
            break
        elif teacherRegex.search(answer) == None:
            print("Incorrect!")
            attempts += 1
            answer = input()
            if attempts == 3:
                print("Out of tries!")

        else:
            print("Correct!")
            answer += 1
            break
    time.sleep(1)

print(f'You got {answer} / {question} correct!')