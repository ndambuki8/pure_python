def odd_even(a):
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        if i % 2 != 0:
            odd.append(i)
    return max(even) - min(odd)

print(odd_even)