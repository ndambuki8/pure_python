from emoji import emojize

def python_snakes(n: int):
    # the loop to determine the number of rows of the pyramid
    for i in range(0, n):
        # The loop that determines the number of columns
        for j in range(n, i, -1):
            # print space between the snake signs
            print(end=" ")
        for k in range(0, i):
            # print the snake emoji
            print(emojize(':snake:'), end=" ")
        print("\n")

python_snakes(7)