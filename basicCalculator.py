import re

print("Our Magical Calculator")
print("Type quit to exit\n")

previous = 0
run =True


def performMath():
    global run
    global previous
    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
        print("Goodbay")
    elif (re.search("[a-zA-Z,:;<>'\"]",equation)):
        print("You should enter a valid equation")
    else:    
        previous = eval(equation)    
        print("You typed", previous)

while run:
    performMath()

