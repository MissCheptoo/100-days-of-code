#bitwise XOR , returns 1 if one of the bits is 1, else it returns 0
a = 10 
b = 9
print(a ^ b)
print(bin(a^ b))

a = 20 
b = 4
print(a & b)
print(bin(a & b) )
print(a |  b)
print(bin(a | b))
print(a ^ b)
print(bin (a ^ b))
print(int(0b10100))

print(~20)

#bitwise right shift
a = 20 
print( a<<2 )
print( a<<3 )

#bitwise left shift
a = 20 
print(a>>2)
print(a>>3)
a = -12
print(a>>1)

#flags
#Read, Write, Execute,  Change Policy

person1 = 0b1000
person2 = 0b1110
person3 = 0b1111
person4 = 0b1010
person5 = 0b1101

together1 = person1 & person2 & person3 & person4 & person5
print(bin (together1))
together2 = person1 | person2 | person3 | person4 | person5
print(bin(together2))

NEURAL_READ = 0b1000
NEURAL_WRITE = 0b0100
NEURAL_EXEC = 0b0010
NEURAL_CHANGE = 0b0001

def myfunction(permission):
    print(bin(permission))

myfunction(NEURAL_WRITE | NEURAL_READ)

a = 10
b = 20
a ^= b
print(a)

def DecimalToBinary(n):
    return("{0:b}".format(int(n)))

d = DecimalToBinary(9)
print(d)

t = bin(14)
print(t)

r = bin(789)
print(r)

def bin_dec(num):
    return int(num,2)

f = bin_dec("11" )
print(f) 

