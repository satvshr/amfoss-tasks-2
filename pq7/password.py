import re
check1 = re.compile(r'[A-Z]')
check2 = re.compile(r'[0-9]')
check3 = re.compile(r'[a-z]')
password = input("Enter your password: ")
mo1 = check1.search(password)
mo2 = check2.search(password)
mo3 = check3.search(password)

try:
    if len (password) >= 8:
        mo1.group()
        mo2.group()
        mo3.group()
        print("Your password is strong")  
    else:
        print("Your password is weak")
except AttributeError:
    print("Your password is weak")


    #check = re.compile(r'(^(.*)?([A-Z])?(.*)?([0-9])?(.*)?([a-z])?$)')
