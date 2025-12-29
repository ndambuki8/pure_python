def even_or_average():
    avg_num = []
    even_number = []
    # using while loop to ensure  code keeps running
    while True:
        number = input("Please enter numbers of choice or done: ")
        avg_num.append(int(number))
        if int(number) % 2 == 0:
            even_number.append(int(number))
            # once the user inputs five numbers the code breaks
        if len(avg_num) == 5:
            break

    if len(even_number) > 0: # checking if list is empty
        return f'The largest even number: {max(even_number)}'
    else:
        return f'The average is: {sum(avg_num) / len(avg_num):.2f}'
    
print(even_or_average())