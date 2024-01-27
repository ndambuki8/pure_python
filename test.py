#RegEx 
#- group()  - returns the part of the string where there is a match

import re

string = '39801 3565, 2102 1111'

pattern = '(\d{3}) (\d{2})'


match = re.search(pattern, string)

if match:
    print(match.groups())
else:
    print("Pattern not found")
