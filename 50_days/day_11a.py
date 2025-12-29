def equal_strings(st1, st2):
    str1 = sorted(st1)
    str2 = sorted(st2)

    if str1 == str2:
        return True
    else:
        return False
    
print(equal_strings('love', 'evol'))