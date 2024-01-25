#RegEx 
#- re.sub()
import re


#multiline string
string = 'abc 12\
    de 23 \n f45 6'

pattern = "\s+"

replace = ''

new_string = re.sub(r'\s+', replace, string, 1)
print(new_string)