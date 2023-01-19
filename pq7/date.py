def leap(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
    else:
        return False
while True:
    import re
    date = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)') 
    a = input("Enter a date in DD/MM/YYYY: ")
    mo = date.search(f'{a}')
    day = str(mo.group(1))
    month = str(mo.group(2))
    if day[0] == "0":
        day.replace(day[0],'')
    if month[0] == "0":
        month.replace(month[0],'')
    year = mo.group(3)
    print(day, month, year)
    if year not in range(1000, 3000):
        print("1")
        print("Enter a valid date.")
    elif month not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"):
        print("2")
        print("Enter a valid date.")
    elif day == "31" and month not in ("1", "3", "5", "7", "8", "10", "12"):
        print("Enter a valid date.")
    elif day == "30" and month not in ("4", "6", "9", "11"): 
        print("Enter a valid date.")
    elif leap(year) == True and day == "29" and month in ("2"):
        print(f"Date you entered: {mo.group(0)} is valid")
        break
    elif leap(year) == False and day == "28" and month in ("2"):
        print(f"Date you entered: {mo.group(0)} is valid")
        break
    else:
        print(f"Date you entered: {mo.group(0)} is valid")
        break

