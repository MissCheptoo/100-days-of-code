#python logical question
#'a3b2c4' --> 'aaabbcccc'
str1 = "a3b2c4"
output= ""
for character in str1 :
    if character . isalpha():
        var = character
    else:
        num =int(character)
        output =output + (var*num)

print(output)
