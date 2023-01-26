def leap(n):

    if n % 4 == 0:
        return True
    elif n % 100 == 0 and n % 400 == 0:
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
    year = int(mo.group(3))
    print(day, month, year)
    if year not in range(1000, 3000):
        print("1")
        print("Enter a valid date.")
    elif month not in ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"):
        print(month)
        print("2")
        print("Enter a valid date.")
    elif day == "31" and month not in ("01", "03", "05", "07", "08", "10", "12"):
        print("Enter a valid date.")
    elif day == "30" and month not in ("04", "06", "09", "11"): 
        print("Enter a valid date.")
    elif leap(year) == True and day == "29" and month in ("02"):
        print(f"Date you entered: {mo.group(0)} is valid")
        break
    elif day == "28" and month in ("02"):
        print(f"Date you entered: {mo.group(0)} is valid")
        break
    else:
        print(f"Date you entered: {mo.group(0)} is not valid")
