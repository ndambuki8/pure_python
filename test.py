import re
#Raw string using r prefix

string = '\n and \r are escape sequences'

result = re.findall(r'[\n\r]', string)
print(result)