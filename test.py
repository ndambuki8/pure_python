#RegEx 
#- Extracting numbers from a string - retaining the string using split
import re
pattern = '\d+'
test_string = 'Twelve : 12 Eighty: 89'
result = re.split(pattern, test_string, 1)

if result:
    print(result)
else:
    print("Search unsuccessful")