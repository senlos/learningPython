
# Capitalization matters. Be care of the first sentence.
print("in python3, print is a function with parentheses")

x = 1

# python don't use braces, but space blocks
if x == 1:
    print("Correct")

# Next look into number type.
# Python is object oriented, and not static.

# try deine a number

y = 2
# print function will auto add an blank between.
print("the value of y is",y)
# depend on the result of calcuate, auto deine types.
z = 5/2
print("the value of z is",z)
# or can explicitly define type by function
a=int(5/3)
print("the value of a is",a)
b=float(7)
print("the value of b is",b)

# Then let's check string type
firstName = 'senlos'
givenName = "Auyeung"
print(firstName,givenName)

# Check operation to number and string
print(a+b)
print(firstName + " " + givenName)

# Assignment can simultaneously
a,b,c = 1,2,3
print(a,b,c)
F,G = 'Senlos', 'Auyeung'
print(F,G)
# don't have to be same type
e,f,g = 218,'hello',886
print(e,f,g)

# operators can only be used within same type
# print(a+F)

# List in python is very easy to use. It can contain all kinds of variable
# Usage is similar to string

# similar way to define list
ll = []
# append method can directly add items to the end of a list
ll.append(1)
ll.append(3)
ll.append(5)
# directly print the whole list
print(ll)
# using loop to print
for x in ll:
    print(x)
# using ordinal to get item of list
print(ll[2])
# using an unexist index will bring an error
# print(ll[4])

# % operator ,returns to the remainder of division
print(11%3)

# ** reflects to power operator
square = 7**2
cube = 2**3
print(square,cube)

# * operator for many repeating
gossip = "bla" * 10
print(gossip)

# also works with list
mix = ["senlos","is",18,"years","old"]
print(mix * 3 )
# list can be joined by + operator
oddNum = [1,3,5]
evenNum = [2,4,6]
num = oddNum + evenNum
print(num)

# tuple is a fixed size list
# string formating
name = "senlos"
print("Hello, %s" % name)
age = 18
print("%s is %d years old" % (name,age))
# argument numbers and types should be matched
# all kind of vairables are ok to formatted as string
print("%s , %s is %s years old" % (name,name,age) )

# %s string, %d integer, %f float, %.<number of digits>f
# %x/%X hexadecimal, base 16. Lowercase and Uppercase
pi = 3.1415926
print("%.2f" % pi)
print("%x" % 43)
print("%X" % 43)

# look more into strings related method
name = 'senlos'
# index method can return the first match occurrence
print(name.index('l'))
# can return part of string with index
print(name[2:4])
# count from the end
print(name[-3])
# len function
print(len(name))
# count method
print(name.count("s"))
# [start:stop:step]
print(name[1:6:2])
# an application is reverse a string
print(name[::-1])
# odd index[1::2]
# uppercase / lowercase method
print(name.upper())
print(name.lower())
# startswith / endswith method
print(name.startswith("sen"))
print(name.endswith('gg'))
# split method, turns string into list
fullname = "Senlos Ouyang"
print(fullname.split(' '))
# conditions. boolean variables
x=2
print(x==2)
print(x==3)
print(x>1)
print(x!=2)
# boolean operator. and or
name = 'senlos'
age = 18
if name == 'senlos' and age ==18:
    print("my name is %s and I'm %d years old." % (name,age))
if name == 'senlos' or 'Jeffrey':
    print('my name is either senlos or Jeffrey')

# in operator
fullname = 'Senlos Ouyang'
if 'Ou' in fullname:
    print('Ou is in fullname')
# if else statement
t = 'Auyeung'
if t in fullname:
    print('%s is in %s' % (t,fullname))
else:
    print("%s isn't in %s" % (t,fullname))
# is operator
x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)
# not operator
print(not False)

# loop structure
primes=[1,2,3,4,5]
for prime in primes:
    print(prime)

# range function
for x in range(5):
    # print out 0,1,2,3,4
    print(x)
# print from >=3 to <6
for x in range(3,6):
    print(x)
# print from >=1 to <10, interect is 3
for x in range(1,10,3):
    print(x)
# besides for loop, there also while loop
count = 0
while count < 5:
    print(count)
    # this operator is like C
    count+=1
# break and continue statement
count = 0
while True:
    print(count)
    count+=1
    if count > 5:
        break

for x in range(10):
    if(x % 2 ==0):
        continue
    print(x)
# else clause for loops
count = 0
while(count<5):
    print(count)
    count+=1
else:
    print('count reached 5')

# function is an important concept, make your code more advanced
def fun1():
    print('this is the first function')
# call function
fun1()
# function can receive arguments
def fun2(name, greet):
    print('%s, %s' % (name,greet))
name = 'senlos'
greet ="hello"
fun2(name,greet)
# function can return a value to caller
def sum(a,b):
    return a+b
print(sum(2,3))

# an example of using functions
def list_benefit():
    return "More organized code", \
    "More readable code", \
    "Easier code reuse", \
    "Allowing programmers to share and connect code together"

def is_benefit(benefit):
    return "%s is a benefit of function!" % benefit

def print_benefit(benefits):
    for benefit in benefits:
        print(is_benefit(benefit))

print_benefit(list_benefit())
###############

# classes and objects
class vehicle:
    name =""
    price=0.00
    # function in class
    def description(self):
        print('%s is worth %.2f.' % (self.name,self.price))
# create object
car1=vehicle()
car1.name='ford'
car1.price=100.01
car1.description()

# dictionary. Similar to list, while index is name.
phonebook={}
phonebook['senlos']=1234567
phonebook['jeffrey']=98755
print(phonebook)
textbook={
'ouyang':1234,
'Auyeung':4321
}
print(textbook)
# delete elements
textbook.pop('ouyang')
print(textbook)
# another delete method
del phonebook['senlos']
print(phonebook)

# module, which should take a specific functionality. It is a file with .py.
# Package, includes modules.
# .pyc a compiled python file
# from  import : import module object to the current namespace
# import * : import all objects from a module
# custom import name
# module initialization. Initialize only once.
# extending module load path.
# environment variable: PYTHONPATH. Can specify addtional directory to look for mudules.
# exploring built-in modules, dir(), help()

# import regular expression module, look for member in the directory, if one's name contains 'find', add to list. print out after sorted.
import re
find_members=[]
for member in dir(re):
    if 'find' in member:
        find_members.append(member)
print(sorted(find_members))

# numpy arrays, which performs better than lists.
height = [1,2,3,4,5,6]
weight = [3,5,7,9,3,5]
import numpy as np
# create numpy array from list
np_height = np.array(height)
np_weight = np.array(weight)
# class 'numpy.ndarray'
print(type(np_height))
print(np_height)
# caculate BMI, Body Mass Index, a measure of body fat in adults
bmi = np_weight / np_height ** 2
print(bmi)
# subsetting,
print(bmi[bmi>1])
# scalar conversion of 2.2lbs per kilogram

# Pandas Basics.
# Pandas is based on numpy, building data structure called DataFrame, which manipulate tabular data with rows as observations and columns as variables.
# One way to create DataFrame is to used dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
# see brics got default index from 0 through 4.
# Also you can define custom index, using index property
brics.index = ['Br','Ru','In',"Ch",'Sa']
print(brics)
# another way to create DataFrame is importing CSV. Which will demonstrate in reViewPandas.py
print(brics.loc['Br'])

# generators, which can produce iterators
from random import randint as rdi
def lottery():
    for i in range(6):
        yield rdi(1,40)
    yield rdi(1,15)

for random_number in lottery():
    print('next number is ... %d' % random_number )

# generator maybe a bit hard to understand.
# one character is 'yield' method
def fibonacci():
    a = 1
    b = 1
    while 1:
        yield a
        a ,b = b , a + b

counter = 0
for n in fibonacci():
    print(n)
    counter += 1
    if counter == 10:
        break
# class generator
print(type(fibonacci()))

# list comprehension, creates a new list, from another using a single-line, readable form.
# got a sentence, split it into single word, count the word's length to make a new list, exclude particular word.
word = 'Today I am not doing anything'
word_split = word.split(' ')
word_count =[]
for single_word in word_split:
    if single_word != 'I':
        word_count.append(len(single_word))
print(word_count)
# list comprehension can simply the upper process.
word = 'I will just lie in my bed'
word_split = word.split()
word_count = [len(single_word) for single_word in word_split if single_word != 'I']
print(word_count)
# create newlist consists of positive numbers from numbers using list comprehension
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [num for num in numbers if num > 0 ]
print(newlist)

# multiple function arguments
def foo(a,b,c, *theRestArguments):
    print('The first argument is %s' % a)
    print('The second argument is %s' % b)
    print('The third argument is %s' % c)
    print('The rest arguments are %s' % list(theRestArguments))
foo(1,2,3,4,5,6,7)

# sending arguments by keywords, then order doesn't matter.
def bar(first, second, third, ** option):
    if option.get('method') == "sum":
        print('Sum is %d' % (first + second + third))
    if option.get('order') == 'first':
        return first
result = bar(1,2,3, method = 'sum', order = 'first')
print(result)
