a=10
b=20
print(a+b)
# output gives 30
#usage of different types of data type
print(type(3>2))
print(type(3))
print(type(3.00))
print(type(True))
print(type("String"))
print(type([]))
my_dict={}
print(type(my_dict))
print(type(33/3))
print(type(3.0/2))
print(type(3!=2))
print(type(3>=2))
print(type(3>2.0))
# taking input in python
x=input("Enter a string input: ")
y=int(input("Enter a integer input: "))
z=float(input("Enter a float input: "))
q=int(input("Enter a integer input: "))
print(x)
print(y)
print(z)
print(q)
#this is a single line comment in python
""" this is a multiline
comment in python"""
''' another way for multiline 
comments in python'''

#conditional statements in python:

# Adding mock variables so the code below executes without NameError
condition = True
statement = "Executing statement"

# if statement
if condition:#if condition is true statement executes the if block else the most next statement after the if block
  print(x)
#if-else
if condition:
  print(statement)
else: 
  print(statement)
  # if block executes if the if condition is true else else statement if be executed bothcan't at same time and else can't be used without else
#if-elif
if condition:
  print(statement)
elif condition:
  print(statement)
elif condition:
  print(statement)
else:
  print(statement)
 # when we want to check diffrerent condition parallely independently checking multiple things then we use if-elif-else statements 

#nested if else:
if condition:
  if condition:
    print(statement)
else:
  if condition:
    print(statement)
  #using inner and outer if else and making it nested is using the indentation in python when we want multiple conditions to be checked dependently on the outer conditions 
# printing the outputs 
# using the keywords of python
