name = "Subhadeep"
age = 19
marks = [80, 75, 90]
is_student = True

total = sum(marks)
average = total / len(marks)

student = {
    "name": name,
    "age": age,
    "marks": marks,
    "is_student": is_student
}

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Student:", is_student)

print("Name type:", type(name))
print("Age type:", type(age))
print("Marks type:", type(marks))
print("Student type:", type(is_student))
print("Dictionary type:", type(student))