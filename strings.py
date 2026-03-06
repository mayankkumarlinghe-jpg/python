my_str = "this is first text"
print(my_str.index('i',3,10)) # 5 as output
my_str ="JamesBOnd 09"
print(my_str.isalnum()) # False as it contains char data too or space
print(my_str.isalnum()) # False as contains num data too or space

my_str = "78.877"
print(my_str.isdecimal()) # returns true but if we use 78.87 it returns false
print(my_str.isdigit()) # returns true but if we use 78.87 it returns false

my_str = "mayank_98"
str1="_mkn89"
str2= "2dnj"
print(my_str.isidentifier())
print(str1.isidentifier())
print(str2.isidentifier())
# True
# True
# False

my_str ="My name is mayank"
print(my_str.islower()) # returns false as M is capital or we can say upper

my_str= "78"
print(my_str.isnumeric()) # returns true but if we use 78.87 it returns false

my_str = "mayank"
print(my_str.isprintable()) # True

my_str=  "   "
print(my_str.isspace())

# stringvariablename.istitle() checks if first letter of string is caps
# stringvariablename.isupper() checks if string is in uppercase

my_set = {"frank","MAyank","Kamboj"}
sep="$$"
print(sep.join(my_set))
# it joins the string with the separators defined by programmer
# stringvariablename.lower() converts string to lowercase and vice versa with the help of uppercase function
# lstrip(character to be removed) function removes the character passed to it
# replace(word to be replaced, number of occurrences to be replaced lets for say 2) function replaces the word
# user wants to replace and we can also specify how many occurrences to be replaced
# rfind("substring") method is used to find the last occurrence of that particular string

my_str = "Mayank is a man"
print(my_str.capitalize()) # capitalize the starting word
print(my_str.casefold()) # lowers all the chars
m = "mayank"
print(m.center(10,"$")) # output $$mayank$$
print(my_str.count("is")) # counts number of times a substring appeared in the string
print(my_str.count("is",7,25)) # we are providing traversing index of string here

my_str="mayank is a man who lives in mohli"
print(my_str.find("mayank")) # output 0 as mayank start from index 0 in this also we can provide start stop index of traversing
print(my_str.endswith("mohli")) # give True as output it checks if string ends with that particular string or not in this also we can provide traversing index

my_str = "M\tayan\tk\t"
print(my_str.expandtabs()) # M       ayan    k        adds more tabs to the string

# rindex() give index of last occurrence of the substring
# rjust(25,"A") justify string to right fills rest of the space of string to left and makes justification of string to right
# rsplit(",",2) splits string to two with separator ,
# rstrip() used to remove characters from right side by passing those chars
# split() method used to remove chars and split string we can also pass number of times we want to perform split
# splitlines() method used to split the string if we pass true to the method it returns line breaks and if we pass true it wont be visible
# swapcase() method swap the cases lower to upper and vice versa
# title() method converts first letter of the each substring to uppercase

my_list =[0,1,2,3,4,5,6,7,8,9]
print(my_list[0])
print(my_list[-2])
# negative indexing
# we can use indexing to traverse our list from end and indexing starts with -1
print(my_list[0:10:1]) # starting with index 0 stops at index 10 means upto 9th index and with step 1

def extract_and_reverse(input_string):
    substring = ''
    substring += input_string[-2:2:-1]
    return substring

# zfill(number) methods helps in adding zeroes in the beginning of the string when we want to make string length more and adding padding as zero
# strip() method is used to remove spaces from beg and end of the string 
# ::1 traverses the string from end to start

# Refactor the following code to improve its efficiency and readability. The code extracts a substring from a given string, starting from the third character to the second last character, and reverses it.
# def extract_and_reverse(input_string):
#     substring = ''
#     for i in range(len(input_string) - 2, 2, -1):
#         substring += input_string[i]
#     return substring

# escape chars in python
# \' helps to insert single quote to string
# \\ insert single backslash
# \n new line to cursor
# \r carriage return takes the cursor to the first position of the same line
# \t add tab space to the string
# \f form feed is a page breaking ascii control character
# \ooo octal value
# \b does backspace of the char
# \xhh hex value 

# unicode and encoding basics
# 'hello'.encode('utf-8') encodes hello string to utf 8 unicode
# output of encode can be decoded using unicode.decode()

def extract_and_reverse_efficient(input_string):
    return input_string[2:-2][::-1]
