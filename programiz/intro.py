# Python list comprehension
# - makes it easy to create a new list based on the values of an existing list.

numbers = [1,2,3,4,5,6]

#syntax of list comprehension
# [expression for item in list if condition == True]


# list comprehension to crate a new list 
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

even_numbers = [num for num in range(1, 10) if num % 2 == 0]

print(even_numbers)

even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]

print(even_odd_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]

print(num_list)

word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)
