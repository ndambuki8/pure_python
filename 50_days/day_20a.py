def capitalize(a: str):
    upper = []
    for i, word in enumerate(a.split()):
        if word[0].islower:
            upper.append(word.capitalize())
        else:
            upper.append(word)
    return ' '.join(upper)

print(capitalize('i like learning'))