if 5>2:
    print("five is greater than two")

    print("hello")
x=5
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#jhkygb (comments) we can comment out things by using ctrl+/
print("this is python")
print('this is python') #in python "" and ''prints same

x=8
y="anshika"
print(type(x))
print(type(y))
x=4.5
print(type(x))

x=""
print(bool(x))#it will show false when string is empty or 0

my_var=40
print(my_var)#we cant use any special character except underscore"_" in any variable naming

x,y,z="30","40","50"
print(x)
fruits=["apple","banana","cherry"]
x,y,z=fruits
x=y=z=fruits
fruits=[2,4,7,8,34,50]
print(fruits)

x="python"
y="is"
z="good"
print(x,y,z)
print(x+y+z)

x=5
x+=3#add and assign which means x=x+3  = x=5+3
print(x)

y=4
y-=2#subtract and assign
print(y)

z=7
z/=4#divide and assign
print(z)

h=3
h*=3#multiply and assign
print(h)

f=6
f%=3#modulus and assign
print(f)
 
x=5
y=10
print(x==y)#equal to

print(x!=y)#not equal

print(x>y)#greater than

print(x<y)#less than

print(x>=y)#greater or equal to

print(x<=y)#less or equal to

x=1j
print(type(x))

X=10
Y=20
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
print(X%Y)
print(X**Y)
print(X//Y)

my_list=["apple","banana"]
print(type(my_list))
print(len(my_list)) #len function gives the length of the  list
print(my_list[1])

my_list=["apple","banana","cherry","sjc","bkdsch","vdjud"]
print(my_list[-5:-2])
print(my_list[-4:0])
print(my_list[-4:])
my_list[1]="mango"
print(my_list)

my_list=["apple","banana",1,3,5,7]
my_list[2:5]="abc"
print(my_list)

my_list=[1,2,4,5,6]
my_list.insert(2,3)
print(my_list)

my_list=[1,2,4,5,6]
my_list.append(3)
print(my_list)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

list1=[1,2,3,"apple",4,5]
list1.remove("apple")
print(list1)

list1=[1,2,3,"apple",4,5]
list1.pop(3)
print(list1)

students={
    "name":"chander",
    "age":30,
    "grades":"A"
    }
print(students)
students["age"]=56
print(students)

students.pop("age")
print(students)

for key,value in students.items():
    print(key,".",value)

    x="good" #global variable

def my_function(): #function opening
    print("python is "+ x)#action

my_function() #function closing

def my_function():
    global x
    x="good"
my_function()
print("function is "+x)


#identity operators
# is     same object     x is y = True
# is not    diff object   x  is not y = true

x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)#true
print(x is z)#false

x=8
y=x
z=10
print(y)
print(z is y)#false
print(x is not y)#false


#program on functions
list1=[1,2,3,4,5,6]
list1.append("apple")#append function will add the element at the nd of the list
list1.insert(3,"banana")#insert function will add the element at a particular position
print(list1)

list1.pop(3)#pop function will remove the the item by indexing
list1.remove("apple")#remove function will remove the item by its name
print(list1)

list2=[7,8]
list1.extend(list2)#extend function add the second list in first list
print(list1)

list1.clear()#clear function gives the empty list
print(list1)


#sorting
list=[1,4,5,8,3,9]
list.sort(reverse=True)
print(list)
list.sort()
print(list)


#strings
text="hello Python"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python","World"))
print(text.split())

x="bob"
y=20
print(f"my name is {x} and my age is {y}")#format string
#to add two different data types we have to use format string


#logical operators
#and     true if both       true and false=false
#or      true if any         true and false=true
#not     reverse value       not true= false  
x=5
print(x>3 and x<10)
print(not(x>3))
print(x>3 or x>10)

#for loop
list1=[1,2,3,4,5]
for x in list1:
    print(x)


#if else statement
    age=20
if age>=18:
    print("You are adult")
elif age==18:
    print("you are teen")
elif age==17:
    print("you are 17")
else:
    print("you are not adult")

x=15
if x>10:
    print("x is greater than 10")

    if x>20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")

x=15
if x%2==0:
    print("x is even")
else:
    print("x is odd")

age=19
if age>=18:
    print("person's age is eligible for driving")
else:
    print("person's age is eligible for driving")

x=5
y=3
z=6
if x>y and x>z:
    print("x is greater than y,z")
elif y>x and y>z:
    print("y is greater than x,z")
else:
    print("z is greater than x,y")

#for loop
word="python"
for x in word:
    print(x)


#range
for i in range(5):
    print(i)
for i in range(1,10,2):
    print(i)

for i in range(1,4):
    for j in range(1,3):
        print(f"i={i},j={j}")

#break statement
for i in range(1,6):
    if i==4:
        break
    print(i)

#question - 1
for i in range(1,21):
    print(i)

#question - 2
for i in range(1,30):
    if i%2==0:
        print(i)

#question - 3
fav=["red","green","peach","blue","black"]
for i in fav:
    print(i)

#question - 5
for i in range(1,10):
    if i==5:
     continue
    print(i)

#question - 6
for i in range(1,10):
    if i==7:
        break
    print(i)

#FUNCTIONS 
def greet():
    print("Hello,Python")
greet()#calling the function

def greet(name):
    print(f"Hello,{name}!")
greet("Alice")
greet("Bob")

#function with return value
def operators(a,b):
    return a+b,a-b,a*b,a/b
result = operators(5,3)
print(result)

#function with default parameter
def greet(name="student"):
    print(f"Hello,{name}!")
greet()
greet("Alice")

#scope of variables
#local variables = declared inside a function , accessible only inside
#global variables = declared outside, accessible everywhere'
x=10
def my_func():
    y=5
    print(x,y)
my_func()
print(x)

#ques 1
def greet():
    print("hello!")
greet()

#ques 2
def add(x,y):
    return x+y
result = add(7,9)
print(result)

#ques 3
x=78
def your_func():
    y=45
    print(x,y)
your_func()
print(x)

#OOPS in python
#class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color}{self.brand} is driving.🚗")

#object
car1 = Car("BMW","Black")
car2 = Car("Tesla","White")

car1.drive()
car2.drive()

#Array
#array is a collection of data of same type
import array
numbers=array.array('i',[1,2,3,4,5])
print(numbers)

#accessing array elements
print(numbers[0])
print(numbers[3])\

 #numpy
from numpy import random
x = random.randint(100)
print(x)
x=random.rand()
print(x)

#ques=generate a 1-D array containing 5 random integers from 0 to 100
from numpy import random
x=random.randint(100,size=(5))#1D array
print(x)

x=random.randint(100,size=(3,5))#2D array
print(x)

x=random.randint(100,size=(2,3,5))# 2D array in which 2 blocks with 3 rows and 5 columns has been made
print(x)

x=random.randint(100,size=(2,3,4,5))
print(x)

#the choice() method allows you to generatera random value based on an array of values
x=random.choice([3,5,7,9])
print(x)

#series in python
import pandas as pd
data=[10,30,30,40]
s=pd.Series(data)
print(s)

#creating a dataframe
import pandas as pd
data = {
    "Name":["Alice","Bob","Charlie","David"],
    "Age":[24,27,22,32],
    "City":["Delhi","Mumbai","Chennai","Kolkata"]
}
df=pd.DataFrame(data)
print(df)

import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)

data={"Math":90,"Science":85,"English":78}
s=pd.Series(data)
print(s) 

# import pandas as pd
# df = pd.read_csv("")
# print(df.head())
# print(df.tail())

