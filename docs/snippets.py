import random
# comment
'''
multiline comment
'''

# Variable, Data type: string, integer, float, boolean
my_name = "John"
print(my_name)
my_int = 1
print(my_int)
my_float = 3.14
print(my_float)
my_bool = True
print(my_bool)

'''
# Arithmetic operators
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

# User input
my_age = 40

# String formating
print(f"Hello, my name is {my_name}, I am {my_age} years old")
print("I don't like ", end="")
print("newlines")

# Collection type: List
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print(grocery_list)
print(grocery_list[0:2])  # 0 to 1 element (2 is non-inclusive)
print(len(grocery_list))
print(grocery_list[-2:])  # from next to last to end
print(grocery_list[::-1]) # reverse list
# [start:end(non-inclusive):step]

# In shell window:
# grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
# dir(grocery_list)
# help(grocery_list.append)

# Collection type: Dictionary
super_villains = {'Fiddler' : 'Isaac Bowin',
                 'Captain Cold' : 'Leonard Snart',
                 'Weather Wizard' : 'Mark Mardon',
                 'Mirror Master' : 'Sam Scudder',
                 'Pied Piper' : 'Thomas Peterson'}
print(super_villains)
print(super_villains['Captain Cold'])
print(super_villains.get('Captain Cold'))

# Conditionals
temp_f = 70
#temp_f = input("Enter temperature in degrees Farenheight (F): ")
temp_f_int = int(temp_f)
if temp_f_int < 30:
    print("Pack long underware")
elif temp_f_int > 100:
    print("Remember to hydrate!")
else:
    print("just right")

# Conditionals: logical operators
if temp_f_int >= 30 and temp_f_int <= 100:
    print("just right")

# Looping: For loop
for x in range(0,10):
    print(x, ' ', end='')
print('\n')
for y in grocery_list:
    print(y)

# Looping: While
random_num = random.randrange(0,100)
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

# Functions
def addNum(first, second):
    sum_num = first + second
    return sum_num
print(addNum(1,4))

# File I/O: open and write
test_file = open("test.txt", "wb") # open for write binary
test_file.write(bytes("Write me to the file\n", "UTF-8"))
test_file.close()
# File I/O: open and read
test_file = open("test.txt", "r+") # open for reading and writing
text_in_file = test_file.read()
print(text_in_file)

# pickle (serialize/unserialize to file (or string)
import pickle

with open("test.pkl", 'wb') as f:
    pickle.dump(grocery_list,f)
    pickle.dump(super_villains,f)
with open("test.pkl", 'rb') as f2:
    a = pickle.load(f2)
    b = pickle.load(f2)
print(a)
print(b)

'''











