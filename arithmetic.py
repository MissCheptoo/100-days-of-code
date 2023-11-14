#Arithmetic operators

a = 10
b = 5

#Adittion
c = a + b
print(c)

#subtraction
d = a - b
print(d)

#multiplication
e = a * b
print(e)

#division
f = a / b
print(f)

#division floor
g = a // b
print(g)

#modulus
h = a % b
print(h)

#power
#exponential
i = a ** b
print(i)

print(5 + 9 - 6  * 10 / 20 )

print((5 + 9)  - 6 * (10 / 20))

fee = 4535

discount_percent = 10

discount_amount = (discount_percent / 100) * fee

discounted_fee = fee - discount_amount

print(discounted_fee)

distance_km = 10
#1 kilometer = 0.621371 miles
distance_km = 10 * 0.621371
print(distance_km)

x = 4
x += 2
print(x)

x *= 3
print(x)

print(9 / (3 + 6) - 1)

for i in range (4) :
    print("A, B , C , D" * (4-1), end="")
    print()

a = ("hello Cheptoo")
print(a[0])
print(a[1:4])
print(a[-1])