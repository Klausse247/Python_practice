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

# name = 'Brad'
# age = 37

#concatenate
#print('Hello, my name is ' + name + ' I am ' + str(age))  # Same thing as is below

#string formatting

#arguments by position
#print('my name is {name} and I am {age}'.format(name=name, age=age))

#F-String V(3.6+)

# print(f'Hello, My name is {name} and I am {age}')

#string methods

# s = 'hello world'

# Capitalize string

# print(s.upper())

# There are plenty of different string methods look them up for refference

#################################################################################

#List is a collection which is ordered and changeable. Allows duplicate members --- similar to arrays

# #creat a list
# number = [1, 2, 3, 4, 5]
# fruits= ['apples', 'pears', 'oranges']

# #use a constructor not as nice
# #numbers2 = list((1, 2, 3, 4, 5))

# print(fruits[1])

# #get length
# print(len(fruits))

# #append list --- adds mangos to list
# fruits.append('mangos')

# print(fruits)

# #remove from list
# fruits.remove('pears')

# print(fruits)

# #insert into a position
# fruits.insert(2, 'Strawberries')

# print(fruits)

# #remove from certain positions using pop

# fruits.pop(2)

# print(fruits)

# #reverse list

# fruits.reverse()
# print(fruits)
# #sort list

# fruits.sort()
# print(fruits)
# #Reverse Sort
# fruits.sort(reverse=True)
# print(fruits)

# #change a value
# fruits[0] = 'Blueberries'

# print(fruits)

###############################################################################################

#A tuple is a collection which is ordered and unchangable. Allows duplicate members.

#Create a tuple

fruits = ('apples', 'oranges', 'grapes')
######fruits2 = tuple(('Apples','oranges'))

#single value needs trailing comma
fruits2 = ('Apples',)


#Get value
#print(fruits[1])


# Can't change the value

##fruits[0] = 'pears'

#delete tuple

del fruits2

print(fruits2)



###print(fruits2, type(fruits2))


# A Set is a collection which is unordered and unindexed. No duplicate members.

