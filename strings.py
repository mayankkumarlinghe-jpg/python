str = "this is first text"
print(str.index('i',3,10))#5 as output
str ="JamesBOnd 09"
print(str.isalnum())#False as it contains char data  too
print(str.isalnum())# False as contains num data too

str = "78.877"
print(str.isdecimal())# returns true but if we use 78.87 it returns false
print(str.isdigit())#retruns true but if we use 78.87 it returns false

str = "mayank_98"
str1="_mkn89"
str2= "2dnj"
print(str.isidentifier())
print(str1.isidentifier())
print(str2.isidentifier())
True
True
False

str ="My name is mayank"
print(str.islower())#returns false as M is capital or we can say upper

str= "78"
print(str.isnumeric())# returns true but if we use 78.87 it returns falsestr = "mayank"
print(str.isprintable())#True

str=  "   "
print(str.isspace())
#stringvariablenmae.istitle() checks if first letter of string is caps
#stringvariablenmae.isupper() checks if string is in uppercase

str = {"frank","MAyank","Kamboj"}
sep="$$"
print(sep.join(str))
it joins the string with the seprators defined by programmer
stringvariablename.lower() converts string to lowercase and vice versa with the help og uppercase function
lstrip(charcter to be removed) function removes the charcter pased to it
replace(word to be replaced,number of occurences to be replaces lets for say 2 )function replace the word
user wants toreplace and we can alsospecify how many occurences to be replaced
rfind("substring") method is used to find the last occurenevce of that perticular string

'''
str = "Mayank is a man"
print(str.capitalize()) #capitalize the starting word
print(str.casefold()) # lowers all the chars
m = "mayank"
print(m.center(10,"$"))# output $$mayank$$
print(str.count("is"))# counts number of times a substring apperared in the string
print(str.count("is",7,25)#we are providing tranversing index of string here

str="mayank is a man who lives in mohli"
print(str.find("mayank"))# output 0 as mayank start from index 0 in this also we can provide start stop index of traversing
print(str.endswith("mohli")) # give True as oyput it checks if string ends with that particular string or not in this also we can provide traversing index

str = "M\tayan\tk\t"
print(str.expandtabs())#M       ayan    k        ads moretabs to the string




rindex() give index oflast occurenec of the substring
rjust(25,"A") justify string to right fills rest of the space of string to left and makes justification of string to right
rsplit(",",2) splits string to two with separator ,
rstrip() used to remove charcters from right side by passing those chars
split() method used to remove chars and spilt string we can also pass number of times we want to perform split
splitlines() method  used to split the string  if we pass true to the method it returns line breaks and if we pass true it wont be visible
swapcase() method swap the cases lower to upper and vice versa
title() method converts first letter of the each subs tring to uppercase

my_list =[0,1,2,3,4,5,6,7,8,9]
print(my_list[0])
print(my_list[-2])
#negati
#we can use indexing to traverse our list from end and indexing starts with -1
print(my_list[0:10:1])# starting with index 0 stops at index 10 means upto 9th index and with step 1
def extract_and_reverse(input_string):
    substring = ''
    substring += input_string[-2:2 :-1]
    return substring


zfile(number) methods helps in
the adding zeroes in the beginning ofthe string when we want to make string lemgth more and adding padding as zero

strip() method is used to remove spaces from beg and en of the string 

#::1 tavers the string from end to start

Refactor the following code to improve its efficiency and readability. The code extracts a substring from a given string, starting from the third character to the second last character, and reverses it.
def extract_and_reverse(input_string):
    substring = ''
    for i in range(len(input_string) - 2, 2, -1):
        substring += input_string[i]
    return substring

\' helps to insert single qoute to string
\\ insert single backslash
\n new line to cursor
\r carriage return takes the cursor to the first position of the same line
\t add tab space to the string
\f form feed is a page breaking ascii controll character
\ooo octal value
\b does backspace of the char
\xhh hex value 
#unicode and encoding basics
'heelo'.encode('utf-8) encodes helo string to utf 8 unicode
               output of encode can be decode usig unicode output.decode()


def extract_and_reverse(input_string):
    return input_string[2:-2][::-1]
escape chars is python
