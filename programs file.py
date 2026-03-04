# Numeric variables - hold integers and decimal values
age = 25
temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
name = "John Doe"
message = 'Hello, world!'

# Boolean variables - only hold the values true and false
is_true = True
is_false = False

# List variables - Stores a collection of items, which can be of different types.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Tuple variables
coordinates = (10, 20)

# Dictionary variables
person = {'name': 'Alice', 'age': 30}

# Set variables
unique_numbers = {1, 2, 3}

# None variable
empty_value = None

#Write a program to check whether a number is positive.
num = int(input("Enter Number"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is 0")
"""Design an algorithm using nested if-else and elif statements to determine the grade of
a student based on their score. The grading scale is: A for 90-100, B for 80-89, C for 70-79, D for 60-69,
and F for below 60.
"""
marks = int(input("Enter the marks of student")
if marks > 0:
            if marks => 90 and marks <=100:
                print("Grade A")
            elif marks = >80 and marks <= 89:
                print("Grade B")
            elif marks => 70 and marks <= 79:
                print("Grade C")
            elif marks => 60 and <= 69:
                print("Grade D")
            elif marks < 60:
                print("Grade F")
else:
    print("Enter valid amrks")

#Loops in Python 
#for loop implemetation using for multiplication program:

for i in range(1,11):
    print(f"9 X {i} = {9*i}")

i=1
while i<11:
    print(f"9 X {i} = {9*i}")
    i+=1
list =[1,2,3,4,5,6,7,8]
result=[]
for item in list:
    if item % 2 ==0:
        pass
    else:
        result.append(item*2)
print(result)

#usage of break and continue
""" the break statement when executed in a loop it terminates the loop from there only and gets the program out of loop 
but sometimes we have to just skip an iteration then we use continue in that case
"""
for i in range(1,20):
    if i%2== 0:
        continue
    if i ==19:
        break
    print(i)
#few uestions on basis of loops 
for j in range(1,4):
        print("*"*j)
for i in range(1,11):
    if i%2==0:
        print("#",end="")
    if i%3==0:
        print("@",end="")
    
    if i%7==0:
        print("~",end="")
    else :
        print(i)
#Nested Loops in the Python
for i in range(1,11):
    for j in range(i,11):
        print("$",end="")
    print(" ")
""" Output 
$ 
$$ 
$$$ 
$$$$ 
$$$$$ 
$$$$$$ 
$$$$$$$ 
$$$$$$$$ 
$$$$$$$$$ """
for i in range(1,11):
    for j in range(1,i):
        print("$",end="")
    print(" ")
"""Output
$$$$$$$$$$ 
$$$$$$$$$ 
$$$$$$$$ 
$$$$$$$ 
$$$$$$ 
$$$$$ 
$$$$ 
$$$ 
$$ 
$ """
list= ["Mango","Apple","grapes","Mongo"]
for fruit in list:
    for word in fruit:
        if word == "M":
            print(fruit)



color =["Red","Green","Blue"]
fruit=["Mango","Apple","grapes","Mongo"]

for x in color:
    for y in fruit:
        print(x,y)
    print()



# for loop with if else statement it execute only when loop doesn't terminate abruptly

fav =['Py','C','java','Ruby']

for lang in fav:
    if 'java' == lang:
        print("Java found")
        break
    else:
        print("Java not Found")

#while loop condition becomes false and loop runs normally then else block will be executed
import random
count =0
while count!=10:
    die= random.randint(1,6)
    if die!=6:
        count+=1
    else:
        print(count)
x=30
y=50
z=10
if x>y or x>z:
    print("x is larger")
else:
    print("x is the smallest")
    
if x>y and x>z:
    print("x is largest")
else:
    print("x is the smallest")

if not(x>y or x>z):
    print("x is not largest")
else:
    print("x is large")

l1=[1,2,3,4,5]
l2=[1,2,4,5]

if l1==l2:
    print(True)
else:
    print(False)
    # returns false


l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

if l1==l2:
    print(True)
else:
    print(False)
# return True

l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

if l1 is l2:
    print(True)
else:
    print(False)

#returns false
"""
import cmath
import numpy as np 

z =3+2j
print(z)

str="My name is MAyank:"
print(str)

first="corey"
last="schafer"

sentance ='my name is {} {}'.format(first,last)
print(sentance)


#string formatting
print(f" my name is {first} {last}")
print(f" my name is {first.upper()} {last.upper()}")
print(f" my name is {first} {last.lower()}")

person = {'name':'mayank','age':39}
sentence ="my name is {} and i am {} years old".format(person['name'],person['age'])
print(sentence)


print(f" my name is {person['name']} and i am {person['age']} years old.")

calc = f'4 times 11 equal to {4*11}'
print(calc)

for i in range(1,11):
    sentence = f'the val is {n:02}'
    print(sentence)
    # it will give padding to the output it will be liek 01 02 03.... upto 9
    

pi = 3.14159265
sentence = f'the val is {pi:.4}'#will give floating point upto 4
print(sentence)

from  datetime import datetime

birthday =datetime(1999,1,1)

#sentence =f'jenn has a birthday on{birthday}'
sentence =f'jenn has a birthday on {birthday:%B %d,%Y}'
print(sentence) #gives basing datetime formating



Microsoft Windows [Version 10.0.19045.6466]
(c) Microsoft Corporation. All rights reserved.

C:\Users\mayan>py -3.13-m pip install numpy
No suitable Python runtime found
Pass --list (-0) to see all detected environments on your machine
or set environment variable PYLAUNCHER_ALLOW_INSTALL to use winget
or open the Microsoft Store to the requested version.
C:\Users\mayan>
C:\Users\mayan>py -3.13 -m pip install numpy
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: numpy in .\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (2.4.2)

C:\Users\mayan>python
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numpy
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    numpy
NameError: name 'numpy' is not defined
>>> import python
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    import python
ModuleNotFoundError: No module named 'python'
>>> import numpy
>>> print(np._version_)
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    print(np._version_)
          ^^
NameError: name 'np' is not defined
>>> import numpy as np
>>> import cmath
>>> z =3+2j
>>> print(z)
(3+2j)
>>> z2 = complex(3,2)
>>> print(z)
(3+2j)
>>> print(z ==)
  File "<python-input-10>", line 1
    print(z ==)
              ^
SyntaxError: invalid syntax
>>> print(z==z)
True
>>> z =3+2j
>>> y=complex(3,2)
>>> print(y==z)
True
>>> print(z.conjugate())
(3-2j)
>>> y=complex(3,2)
>>> z =3+2j
>>> z1=1+3j
>>> z3=4+5j
>>> z5=z1+z2
>>> print(z5)
(4+5j)
>>> z5=z1*z3
>>> print(z5)
(-11+17j)
>>> z5=z1/z3
>>> print(z5)
(0.4634146341463415+0.17073170731707324j)
>>> z3=4+5j
>>> abs(z)
3.605551275463989
>>> cmath.phase(z)
0.5880026035475675
>>> print(np.arctan2(4,5)
... )
0.6747409422235526
>>> cmath.phase(z3)
0.8960553845713439
>>> print(np.arctan2(4,5))
0.6747409422235526
>>> print(np.arctan2(5,4))
0.8960553845713439
>>> x=cmath.polar(z3)
>>>
>>> print(x)
(6.4031242374328485, 0.8960553845713439)
>>> z=cmath.rect(x)
Traceback (most recent call last):
  File "<python-input-36>", line 1, in <module>
    z=cmath.rect(x)
TypeError: rect expected 2 arguments, got 1
>>> z=cmath.rect(x[0],x[1])
>>> print(z)
(4+4.999999999999999j)
>>>
KeyboardInterrupt
>>>
"""


