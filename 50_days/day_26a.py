def sort_words(sentence):
    list1 = []
    sentence = sentence.replace(' ', '')
    for i in sentence:
        if i not in list1:
            list1.append(i)
    list1.sort()
    sorted_words = [','.join(list1)]
    return sorted_words

print(sort_words('love life'))