#RegEx 
#- A regular expression is a sequence of characters that defines a search apptern
#eg. !a....s$
import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Search successful")
else:
    print("Search unsuccessful")