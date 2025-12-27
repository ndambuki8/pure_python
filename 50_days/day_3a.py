register = {'Michael':'yes', 'John':'no', 'Peter':'yes', 'Mary':'yes'}

def register_check(reg: dict):
    # create a count variable
    count = 0
    for value in reg.values():
        if value == 'yes':
            count += 1
    return 'Number of students in school is', count

print(register_check(register))

# or

register = {'Michael': 'yes', 'John':'no', 'Peter':'yes', 'Mary':'yes'}

def register_check2(reg: dict):
    count = 0
    for value, key in reg.items():
        if value == 'yes':
            count += 1
    return 'Number of students in school is', count
