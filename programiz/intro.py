student = ["Jack", 32, 'Computer Science', [2,4]]

student.append(77)
student.insert(3, "Buda")
student[3] = "Jabaaa"
student.remove(77)

del student[0]
del student[1:4]

more = ["Jane", 45, "loves cooking", [24,8]]

student.extend(more)
print(student)
# print(student[-5])
# print(student[0])
