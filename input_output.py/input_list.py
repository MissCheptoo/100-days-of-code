n = int(input("length of list:"))
list = []

for i in range (n):
    element = int(input("enter the element:"))
    list.append(element)

print("list elements are:" , list)


list = []

while True:
    element = int(input("enter the element:"))
    list.append(element)
    Choice = (input(" want to stop? if yes press yes otherwise press any key"))
    if Choice == "yes":
        break
print("list elements are:",list)

import ast
list = []

while True:
    element = ast.literal_eval(input("enter the element:"))
    list.append(element)
    Choice = (input(" want to stop? if yes press yes otherwise press any key!"))
    if Choice == "yes":
        break
print("list elements are:",list)

n = (input("element with space"))
list = n.split()

print(list)

import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print(z)