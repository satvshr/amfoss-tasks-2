import pyinputplus as pyp
ingredients = {'wheat' : 50,
'white' : 40,
'sourdough' : 60,
'chicken' : 20,
'turkey' : 25,
'ham' : 40,
'tofu' : 30,
'cheddar' : 10,
'swiss' : 20,
'mozzarella' : 15,
'mayo' : 10,
'mustard' : 10,
'lettuce' : 15,
'tomato' : 15}

sandwich = []
print("Choose your type of bread: ")
sandwich.append(pyp.inputMenu(['wheat', 'white', 'sourdough'], numbered=True))

print("Choose a type of meat: ")
sandwich.append(pyp.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True))

a = pyp.inputYesNo("Do you want cheese? (y/n): ",allowRegexes=['yes','no'])
if a == 'yes':
    sandwich.append(pyp.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True))
    
    
x = pyp.inputYesNo("Do you want mayo?")
if x == 'yes':
    sandwich.append('mayo')
x = pyp.inputYesNo("Do you want mustard?")
if x == 'yes':
    sandwich.append('mustard')
x = pyp.inputYesNo("Do you want lettuce?")
if x == 'yes':
    sandwich.append('lettuce')
x = pyp.inputYesNo("Do you want tomato?")
if x == 'yes':
    sandwich.append('tomato')

num = pyp.inputInt("Enter number of sandwiches: ", min=1)

price = 0
for i in sandwich:
    price += (ingredients[i] * num)

print("THe combined price for everything is: ", price)




