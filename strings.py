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


