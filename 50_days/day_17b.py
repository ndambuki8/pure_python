def sort_length(arr: list):
    for item in range(len(arr)):
        for j in range(len(arr)-1):
            #3 check if any of the words is longer than the other
            if len(arr[j]) > len(arr[j+1]):
                # swap the longest for the shortest
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

names = ["Peter", "Jon", "Andrew"]

print(sort_length(names))