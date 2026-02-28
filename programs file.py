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
