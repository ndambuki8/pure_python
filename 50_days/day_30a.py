from collections import Counter

name = ["John", "Peter", "'John", "Peter", "Jones", "Peter"]

def frequent_name(a):
    return max(Counter(a).most_common())