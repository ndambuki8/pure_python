def same_in_reverse(a):
    if a == a[::-1]:
        return True
    else:
        return False
    
print(same_in_reverse('dad'))