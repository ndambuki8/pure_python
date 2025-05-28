student = ["Jack", 32, 'Computer Science', [2,4]]
# print(student)

for item in student:
    if item == 32:
        continue
    for it in item:
        print(it)
    # print(item)