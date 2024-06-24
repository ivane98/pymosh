# from converters import kg_to_lb, lb_to_kg
# from utils import find_max
# import ecommerce.shipping

# from random import randint

# price = 1000000
# down_payment = 0
# good_credit = True

# if good_credit:
#     down_payment = price * 0.1
# else:
#     down_payment = price * 0.2

# print(down_payment)

# name = input('input a name: ')

# if len(name) < 3:
#     print('name must be at least 3 chars long')
# elif len(name) > 50:
#     print('name must be less then 50 chars long')
# else:
#     print('name looks good')

# weight = int(input('Weight: '))
# unit = input('(L) for pounds and (K) for kg').lower()

# if unit == 'l':
#     print(f'you are {weight / 2.2}kg')
# else:
#     print(f'you are {weight * 2.2} pounds')

# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print('done')

# num = 9
# count = 0
# limit = 3

# while count < limit:
#     guess = int(input('guess: '))
#     count = count + 1
#     if guess == num:
#         print('congrats, you won')
#         break
# else:
#     print('you lost')

# command = ''
# started = False

# while command != 'quit':

#     command = input('>').lower()

#     if command == 'help':
#         print('start - start the car')
#         print('stop - stop the car')
#         print('quit - exit the game')
#     elif command == 'start':
#         if started:
#             print('car is already started')
#         else:
#             started = True
#             print('car started...')
#     elif command == 'stop':
#         print('car stopped')
#     elif command == 'quit':
#         break
#     else:
#         print('sorry i dont understand that')


# prices = [10, 20, 30]

# sum = 0

# for i in prices:
#     sum = sum + i

# print(sum)

# numbers = [2, 2, 10, 2, 11]
# num = 0
# for i in numbers:
#     if i > num:
#         num = i

# print(num)
        
# l = [1, 1, 2, 2, 3, 3, 5, 5]
# uniques = []

# for i in l:
#     if i not in uniques:
#         uniques.append(i)

# print(uniques)

# coord = (1, 2, 3)

# x, y, z = coord

# print(x, y, z)

# convert = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four'
# }

# phone = input('Phone')
# output = ''

# for i in phone:
#     output += convert[int(i)] + ' '

# print(output)

# try:
#     age = int(input('Age: '))
#     income = 1000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('cant devide by zero')
# except ValueError:
#     print('Invalid Value')

    
# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name

#     def talk(self):
#         print(f'my name is {self.name}')

# p = Person('john')
# p.talk()

# class Animal:
#     def walk(self):
#         print('walking')

# class Dog(Animal):
#     pass

# d = Dog()
# d.walk()
        
# numbers = [1, 2, 3, 4]

# print(find_max(numbers))



# class Dice:
#     def roll(self):
#         x = randint(1, 6)
#         y = randint(1, 6)
#         return (x, y)
    
# d = Dice()
# print(d.roll())


from pathlib import Path

path = Path('email')

for file in path.glob('*'):
    print(file) 