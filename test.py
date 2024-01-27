#RegEx 
#- re.search(patterb, str)

import re

string = 'Python is fin'

#check if 'Python' isat the beginning 
match = re.search('\APython', string)

if match:
    print("pATTERN FOUND INSUDE")
else:
    print("Pattern not found")

