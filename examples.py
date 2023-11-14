#write a python program to print duplicates present in a list
l  = ["hello",10, 20, 40, 20, 60, 40, 30]
duplicate = []
for element in l :
    if l .count(element)>1:
         duplicate.append(element)

print(duplicate)

l  = ["hello",10, 20, 40, 20, 60, 40, 30]
duplicate = []
for element in l :
    if l .count(element)>1 and element not in duplicate:
         duplicate.append(element)

print(duplicate)

l  = ["hello",10, 20, 40, 20, 60, 40, 30]
duplicate = []
for i in range (len(1)):
     for j in range(i +1,len(l)):
          if l[i] == l[j] and l[i] not in duplicate:
               duplicate.append(l[i])

print(duplicate)
