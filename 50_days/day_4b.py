def word_index(arr: list):
    for word in arr:
        for j in range(len(arr) - 1):
            # checking if the lengths of all the words are equal
            if len(arr[j]) == len(arr[j + 1]):
                return 0
            
            # using len function and max to find the longest word
            elif len(word) == len(max(arr)):
                # using list method index to find index of longest word
                return f'Longest word is at index: {arr.index(word)}'
            

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]
words3 = ["Love", "Hate", "perspiration"]

print(word_index(words1))
print(word_index(words2))
print(word_index(words3))