morning_batch = [101, 102, 103, 103, 104, 105]
evening_batch = [103, 104, 106, 107]

# Remove duplicates
morning_set = set(morning_batch)
evening_set = set(evening_batch)

print("Unique morning IDs:", morning_set)
print("Common students:", morning_set & evening_set)
print("All unique students:", morning_set | evening_set)
print("Only morning students:", morning_set - evening_set)

# Add a new student
morning_set.add(108)

# Remove a student safely
morning_set.discard(999)

print("Updated morning batch:", morning_set)