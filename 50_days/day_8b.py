def prime_numbers() -> list:
    prime_num = []
    n = int(input('Please enter a number (integer): '))
    # creating a range of the input number
    for i in range(0, n + 1):
        if i > 1:
            for j in range(2, i):
                # if the number in the range is divisible by j
                # then the number is not a prime
                if i % j == 0:
                    break
            else:
                prime_num.append(i)

    return prime_num

print(prime_numbers())