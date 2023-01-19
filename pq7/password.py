import re
check = re.compile(r'((?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{8}$)')
password = input("Enter your password: ")
mo = check.search(f'{password}')
try:
    print(mo.group()+" is a strong password")  
except AttributeError:
    print("Your password is wrong")