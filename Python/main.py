""" import math

first_name = "Luka"
age = 18

print(first_name)

print(f"Hello {first_name}")

print(f"Your name is {first_name} and your age is {age}")

student = False

if student:
    print(f"Fuck you {first_name} of age {age}")
else: 
    print(f"Still fuck you {first_name}")

name = "Luka Cassar"
goesGym = 12
gpa = 4.9

gpa = int(gpa)
print(f"Your GPA is definitely not {gpa}")

if type(goesGym) is bool:
    print("That goesGym better be true")
else:
    goesGym = bool(goesGym)
    goesGym = True
    print(f"I made it true anyway :) {goesGym}")

    study = input("What do you study? ")

    print(f"I like {study}")
    
    if study == "Computer Science":
        print("Best Course")

    radius = input("Enter radius of circle ")
    radius = int(radius)
    radius = 3.14 * radius * radius

    print(f"The radius of the circle is approx {radius} ") 

item = input("What do you wish to buy? ")
price = float(input("What is the price of that item? "))
quantity = int(input("How many? "))

total = price * quantity

print(total) 

friends = 30
friends = friends ** 2
print(f"Just increased your friends to {friends}")

print(f"Why is the ^ operator a subtraction! {friends ^ friends} just removed ur friends lol") 

radius = float(input("Now give me the radius of a circle we usin math class "))
area = math.pi * pow(radius, 2)
print(f"The area is {round(area, 2)} (circle btw) ") 

print("Enter values a and b")
a = float(input())
b = float(input())

c = int(math.sqrt(a**2 + b**2))

print(f"The hypotenuse is {c}") 

name = input("Enter your full name ")
len = len(name)
name = name.capitalize()
print(name)
print(f"The first instance of r is at position {name.find("r")}")

res = name.isdigit()
print(f"Is your name only digits? {res}")     """  

""" sen = input("Enter a sentence for analysis ")
print(f"Sentence is {len(sen)} characters long ")
tempsen = sen.replace(" ", "")
print(f"Without spaces, sentence is {len(tempsen)} characters long ")


spaceCount = 0
tempsen = sen
while not (tempsen.find(" ") == -1):
    spacePos = (tempsen.find(" "))
    tempsen = tempsen[spacePos + 1:]
    spaceCount += 1
print(f"The sentence has {spaceCount} spaces")  """   

""" bank = {"Alan" : 50000,
        "Bob" : 30000,
        "Charles" : 45999
        }

get = input("Alan, Bob or Charles?")
print(bank.get(get)) """

""" foods = {"piz" : 4,
         "nacho" : 5,
         "potato" : 4.39,
         "soda" : 3}

cart = []

print("-----MENU-----")
for k,v in foods.items():
    print(f"Item {k} costs ${v:.2f}")
print("-----")

while True:
    item = input("Select an item, q to quit").lower()
    if item =="q":
        break
    cart.append(item)
print("Your order: ")
for i in cart:
    print(i)

for i in cart[:]:
    if i in foods:
        print(f"Item {i} has been saved to cart")
    else:
        cart.remove(i)
        print(f"Invalid item. Item {i} has been removed from the cart")

total = 0
for i in cart:
    total += foods.get(i)

print(f"Your total is ${total:.2f}") """
    
import random

""" dice = random.randint(1,6)
print(dice)
 """

""" danger = [0,1,0,0,1,1,1,0,1,0,1,1,0,1]
maxpts = len(danger)
pts = 0
random.shuffle(danger)
print(danger)
while True:
    for i in danger:
        guess = input("Can you guess the next number? 0 or 1 ")
        guess = int(guess)
        if i == guess:
            print("Nice ")
            pts += 1
            if pts == maxpts:
                break
            
        else:
            print("Restarting... ")
            break
    if pts == maxpts:
        print("Ya fuckin won")
        break
 """

