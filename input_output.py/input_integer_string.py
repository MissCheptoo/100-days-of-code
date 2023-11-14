def isValidInt(input):

    if input[0] == '-':
        return input[1:].isdigit()
    else:
        return input.isdigit()
    
userinput = "5"
print(isValidInt(userinput))

#change the user input to different data types

n = (input("enter a string: "))

try:
    int( n)
except ValueError:
    print("string is not an integer")
else:
    print("string is an integer")

n = (input("enter any integer: "))
while True:
    if n.isdigit():
        print("thanks for entering an integer")
    else:
        print("you have not entered an integer")
