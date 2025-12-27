students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def count_students(arr: list) -> list:
    # create an empty list to append lowercase strings
    new_list = []
    student_count = []

    # converting names to lowercase and appending to a new_list
    for names in students:
        new_list.append(names.lower())

    # Finding and counting all males in the list and putting it in a tuple
    for sex in new_list:
        if sex == "male":
            student_count.append((sex, new_list.count(sex)))
            break
    
    # Finding and counting all females in the list and putting it in a tuple
    for j in new_list:
        if j == 'female':
            student_count.append((j, new_list.count(j)))
            break
            # returning a tuple of students

    return student_count


print(count_students(students))
