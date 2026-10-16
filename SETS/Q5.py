python_students = [101, 102, 103, 104, 105, 105]
ml_students = [103, 104, 105, 106, 107, 107]

# Convert lists into sets
python_set = set(python_students)
ml_set = set(ml_students)

# 1. All unique students
print("All unique students:", python_set | ml_set)

# 2. Common students
print("Common students:", python_set & ml_set)

# 3. Only Python students
print("Only Python students:", python_set - ml_set)

# 4. Students enrolled in only one course
print("Only one course students:", python_set ^ ml_set)