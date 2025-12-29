import string

str1 = 'leArning is hard, bUt if you appLy youRself you can '\
        'achieVe success'

upper_names = []

for word in str1.split():
    for letter in word:
        # using a string module to find an uppercase letter
        if letter in string.ascii_uppercase:
            upper_names.append("".join(word[::-1]))

print(upper_names)