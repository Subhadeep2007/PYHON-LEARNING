student1 = {"coding", "gaming", "music", "cricket"}
student2 = {"coding", "reading", "music", "football"}

# 1. All unique hobbies
print("All hobbies:", student1 | student2)

# 2. Common hobbies
print("Common hobbies:", student1 & student2)

# 3. Only Student 1 hobbies
print("Student 1 only:", student1 - student2)

# 4. Non-common hobbies
print("Non-common hobbies:", student1 ^ student2)