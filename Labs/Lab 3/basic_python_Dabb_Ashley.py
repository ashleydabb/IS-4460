#this is a comment

#literals
print("Hello World!")
print("Hello Class")
print('Chewyy')
print(88.88) 


#line syntax
a = 9
b = 6
print ("a + b =",a+b)

#variable names
A = 4
a = 8
student_gpa = 4.0
user_name = "Chewyy"
gpa = 3.8

#print variables
print(user_name)
print(gpa)
print(A)
print(a)

print("A = ", type(A))
print("GPA = ", type(4.0))

#string concatenation - two different ways ++ or {}
print("My name is " + user_name + " not Bob")
print(f"My name is {user_name} not Bob")

#variable typing
number = 54321 * 19876 #changed numbers
print(str(number)[3:7]) # use str() to convert the number to a string. use [1:3] to get the first 3 numbers

  
#functions
def add_numbers (a,b):
    output = a + b
    return output 

print(a+b)
print(b)
    
#function arguments
def add_numbers(a,b):
    output = a + b
    return output
print(add_numbers(3,4)) # positional arguments.
print(add_numbers(b=7,a=3)) # named arguments

#variable scope
name = "Jordan"

#say_hello function
def say_hello():
  name = "Ash"
  print(name)
  say_hello()

#true/false statements boolean
print(f"a: is 40 gt 10? {24>10}")
print(f"b: is 15 lt 2? {15<2}")
print(f"c: {2 == 2}")
print(f"d: {2 > 24}")

#boolean as int
print(f"one is equal to 4:",int(4==6))
print(f"one is equal to 8:",int(8==8))

#literals and variables
myname = "Ashley"
myage = 21
print(f"a: {66}") #numeric literal
print(f"b: {'Hello'}") #string literal
print(f"c: {False}") #constant literal
print(f"d: {myname}") #String variable
print(f"e: {myage}") #numberic variable

#precedence math
print((2-3+5),(6-8+9))
print((2*3+5),(6*8+9))

#relational operators
print(f"is 'ash'=='ashley'? {'ash'=='ashley'}")

#equality operator
my_name = "ash"
print("assignment: ",my_name)
print("equality: ",my_name == "ash")

#comparison operator
print("comparison:","aa" < "b")
print("comparison:", 8, 15)

a = 0
b = 1
print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a < b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

#if statement & elif 
bank_balance = 400
if bank_balance < 200:
    money = 1000
    bank_balance += money
else:
    print("balance is less than or equal to 200")


check_balance = 700
savings = 18
if check_balance < 500:
    money = 6000
    check_balance += money
elif check_balance > 300:
    savings += 100
    check_balance -=50
else:
    savings += 75
    check_balance += 75
print("Check Balance = ",check_balance)
print("Savings Amount = ", savings)


#ternary operator
fuel = 1
print("Fill tank now" if fuel <= 1 else "Theres enough fuel")


#while loop
fuel = 19
while fuel > 1:
    #keep driving baby!!!
    print("There's ENOUGH fuel!")
    fuel -= 1

#for loop
books = ['Percy Jackson','The little engine that could','National parks rock!']
for book in books:
    print(f"book: {book}")

for i in range(4):
    print(f'i: {i}')

#for loop break
for count in range (16):
    print(f"{count} times 2 is {count * 2}")
    if count == 13:
        break

#for loop continue
for count in range(16):
    if count == 13:
        continue 
    print(f"{count} times 2 is {count *2}")

    
    
#fun stuff
print(f"{name} loves to snowboard with {user_name}")