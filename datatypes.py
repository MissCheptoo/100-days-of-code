num = 2.5
print(type(num))

num = 5
print(type(num))
num = -5
print(type(num))

num = 6 + 9j
print(type(num))

a = 5.6
b = a
print(b)

c = 5
k = float(c)
print(k)
d = complex(b+c)
print(d)
print(a>c)

print(int(True))
print(int(False))

c = [1, 2, 3, 4]
print(type(c))

x = {1, 2, 3, 4}
print(type(x))

t = (1, 2, 3, 4)
print(type(t))

p = 'cheptoo'
print(type(p))

k = "a"
print(type(k))

f =  range(10)
print(type(f))

for i in range (1) :
    for j in range (4 ):
        print("A, B, C ")

print()

 
d = {"navin":"samsung", "rahul":"iphone","cheptoo":"oppo"}
print(d)
print(d.get("cheptoo"))
d ['name'] = 'mercy'
print(d)
d.update({ "navin":"samsung", "rahul":"iphone","mercy":"oppo"})
print(d)

multiline = """The ice cream vanquished my longing for sweets, upon this diet I look away, it no longer exists on tis day"""
print(multiline)

icecream = ['cookie','vanilla']
icecream.append('salted caramel')
print(icecream)
icecream[0]= 'chocolate'
print(icecream)

d = {1, 2, 1, 3, 3, 4, 1, 5, 31, 6, 3, 2}
print(d)
p = {1, 2 , 7, 9, 10, 25, 12, 5, 7, 8,9}
print(d | p)
print(d & p)
print(d - p)
print(p - d)
print(d ^ p)

split1 = "This, is, orange"
s = split1.split(",")
print(s)
print(type(s))
print( s*2)
s = split1.strip()
print(s)

#binary data types
x = b'cheptoo'
print(x)
print(type(x))
print(x[4])
print(x[5])
print(x[-2])

first = "Cheptoo"
last = "Mercy"

print(type(first))
print(type(first) == str) 
print( isinstance (first, str)) 

print(first)
print(first.lower())
print(first.upper())

multiline = "I love you Cheptoo"
print(multiline)
print(multiline.title())
print(multiline.replace("good","ok"))

print(len(multiline))
print(len(multiline.strip()))

#building a menu
title = "menu".upper()
print(title.center(10,"="))
print(title.center(20,"="))
print("Coffee".ljust(16,".") +"$1".rjust(4))
print("Muffin".ljust(16,".") +"$3".rjust(4))
print("Salted Caramel".ljust(16,".") +"$4".rjust(4))


first = "Cheptoo"
print(first.startswith("C"))
print(first.endswith("o"))

gpa = 3.28
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

import math

print(math. sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode = "10001"
print(type(zipcode))
zip_value = int(zipcode)
print(type(zip_value))

a = "I love coffee"
i = print(type(a))
print(i)