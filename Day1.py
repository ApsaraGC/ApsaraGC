print("Hi Nanu")
print('o_ _')#python executing  line by line code
print('*' * 10) # output ********
# web developer : learn html,css, javascript ,Django is popular python framework
# 2 hours/Day (3 month)

#variables
price=5
price=10
print(price)# first read 5 and finally print 10

import sys
print(sys.version)#check the python version 
cash=10
rate=4.4
name='Nanu'
is_value=True
print(cash)

full_name='Hanag'
age=22
is_new=True
character=' python'
print(character[2])
 
#receive input from user
name= input('What is your name? ')#input function
print(' Hi '  +  name)

person_name=input ('Your name ')
color=input('write your favorite color  ')
print(person_name + ' like ' + color)

#Type conversion
birth_year=int(input('Birth year:'))
age=2018 - birth_year
#age= 2018 -int(birth_year)
print(type(age))
print(age)

weight_lbs=int((input('What is your weight:')))
weight_kg= weight_lbs * 0.45
print(weight_kg )

#string
course='python course'
print(course)

String_value='''
hi nanu
k xa 
'''
print(String_value)

character='python'
print(character[2])#index start from 0
print(character[0:3])#output pyt


#format string
first='maya'
last='mimi'
message= first + last
#message= first + '[' + last + '] is a coder
msg=f'{first} [{last}] is a coder'
print(msg)
print(message)

count='number of length'
print(len(count))
print(count.upper())
print(count.find('num'))
print(count.replace('number', 'python'))

#arithmetic operations
print(10 +2)
print(9/2)#4.5
print(9//2)#4
print(10 **2)#power 100

x=10
x +=3
print(x)#13

y=1 + 2 *2#5
print(y)

z=10 +3 *2 **2# first ** 22
print(z)

#math function
a=2.9
print(round(a))#3

import math
print(math.floor(2.9))# 2