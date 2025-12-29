def any_num(*args):
    ave = sum(args)/len(args)
    return f'The avaerage is {ave}'


print(any_num(12,90,10))