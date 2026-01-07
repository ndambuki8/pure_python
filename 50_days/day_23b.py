import math

def multiply_words(s: str):
    arr = []
    for word in s.split():
        if word.islower():
            arr.append(len(word))
        
        # using the math prod to multiply the lengths
        m = math.prod(arr)
    return 'The prod of the word length is', m

# strings
str2 = "Love live and laugh"
str3 = "Hate war love peace"

print(multiply_words(str2))
print(multiply_words(str3))