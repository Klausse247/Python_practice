#basic variables
# x = 1           # Int
# y = 3.6         #float
# name = 'Kevin'  #string
# a_bitch = True  #bool

#multiple assignments to different variables
# x, y, name,  a_bitch = (1, 3.6, 'Kevin', True)

# # print (x, y)

# # Basic Math Equations
# a = x + y

# #Casting

# x = str(x)
# y = int(y)
# z = float(y)

# print(type(y), type(z), z)

#################################################################################

#Strings in python are surrounded by either single or double quotes. Lets look at string formatting and some strings

name = 'Brad'
age = 37

#concatenate
#print('Hello, my name is ' + name + ' I am ' + str(age))  # Same thing as is below

#string formatting

#arguments by position
#print('my name is {name} and I am {age}'.format(name=name, age=age))

#F-String V(3.6+)

print(f'Hello, My name is {name} and I am {age}')

#string methods

s = 'hello world'

# Capitalize string

print(s.capitalize())


