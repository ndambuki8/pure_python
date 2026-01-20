s = 'Hi my name is Richard'

def string_length(s: str) -> dict:
    list1 = []
    dict1 = {}

    # converting string into a list of strings
    for word in s.split():
        list1.append(word)
        # update the dictionary with word lengths
    for word in list1:
        dict1.update({word: len(word)})
    return dict1

print(string_length(s))