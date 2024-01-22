#RegEx 
#- Extracting numbers from a string
import re
pattern = '\d+'
test_string = 'hello 12 hi 89. hOWDY 34'
result = re.findall(pattern, test_string)

if result:
    print(result)
else:
    print("Search unsuccessful")