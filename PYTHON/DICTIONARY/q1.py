# ============================================================
#              PYTHON DICTIONARY PRACTICE
#       LEVEL 1 + LEVEL 2 + LEVEL 3 + CHALLENGE
# ============================================================

# A DICTIONARY stores data in KEY : VALUE pairs.
#
# Example:
#
# student = {
#     "name": "Rahul",
#     "age": 25,
#     "city": "Pune"
# }
#
# "name", "age", "city" -> KEYS
# "Rahul", 25, "Pune"   -> VALUES
#
# Dictionaries are:
# - Mutable -> we can change them
# - Ordered in modern Python
# - Keys must be unique
# - Values can be duplicated
# - Accessed using keys, NOT indexes


# ============================================================
# LEVEL 1 - DICTIONARY BASICS
# ============================================================


# ------------------------------------------------------------
# Q1. Create and print a dictionary
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# Print the complete dictionary
print("Q1 - Student:", student)


# ------------------------------------------------------------
# Q2. Access values using keys
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# Use the key to access its value
print("Q2 - Name:", student["name"])
print("Q2 - Age:", student["age"])
print("Q2 - City:", student["city"])


# ------------------------------------------------------------
# Q3. Find the number of items in a dictionary
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# len() tells how many key-value pairs exist
print("Q3 - Length:", len(student))


# ------------------------------------------------------------
# Q4. Add a new key-value pair
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25
}

# Add a new key and value
student["city"] = "Pune"

print("Q4 - After adding city:", student)


# ------------------------------------------------------------
# Q5. Change an existing value
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# Change the value of age
student["age"] = 26

print("Q5 - Updated student:", student)


# ------------------------------------------------------------
# Q6. Remove a key-value pair using pop()
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# pop() removes the specified key
student.pop("age")

print("Q6 - After removing age:", student)



# ------------------------------------------------------------
# Q7. Get a value safely using get()
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25
}

# get() returns the value if the key exists
print("Q8 - Name:", student.get("name"))

# If key doesn't exist, get() returns None
print("Q8 - City:", student.get("city"))


# We can also provide a default value
print(
    "Q8 - Country:",
    student.get("country", "Not available")
)


# ------------------------------------------------------------
# Q8. Get all keys
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# keys() returns all dictionary keys
print("Q9 - Keys:", student.keys())


# ------------------------------------------------------------
# Q9. Get all values
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# values() returns all values
print("Q10 - Values:", student.values())


# ------------------------------------------------------------
# Q10. Get key-value pairs using items()
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# items() gives both key and value
print("Q11 - Items:", student.items())


# ------------------------------------------------------------
# Q11. Loop through dictionary keys
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# By default, a dictionary loop gives keys
for key in student:
    print("Q12 - Key:", key)


# ------------------------------------------------------------
# Q12. Loop through dictionary values
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

for value in student.values():
    print("Q13 - Value:", value)


# ------------------------------------------------------------
# Q13. Loop through keys and values
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}

# items() gives key and value together
for key, value in student.items():
    print("Q14 -", key, ":", value)


# ============================================================
# LEVEL 2 - DICTIONARY LOGIC
# ============================================================


# ------------------------------------------------------------
# Q14. Create a dictionary from two lists
# ------------------------------------------------------------

keys = ["name", "age", "city"]
values = ["Rahul", 25, "Pune"]

# zip() pairs items from both lists
student = dict(zip(keys, values))

print("Q15 - Dictionary:", student)


# ------------------------------------------------------------
# Q16. Find the sum of dictionary values
# ------------------------------------------------------------

marks = {
    "Math": 80,
    "English": 75,
    "Science": 90
}

total = 0

# Loop through only the values
for mark in marks.values():

    # Add each mark to total
    total = total + mark

print("Q16 - Total marks:", total)


# ------------------------------------------------------------
# Q17. Find average marks
# ------------------------------------------------------------

marks = {
    "Math": 80,
    "English": 75,
    "Science": 90
}

total = 0

for mark in marks.values():
    total = total + mark

# Average = total / number of subjects
average = total / len(marks)

print("Q17 - Average:", average)



# ------------------------------------------------------------
# Q20. Count how many students passed
# ------------------------------------------------------------

marks = {
    "Rahul": 80,
    "Amit": 45,
    "Raj": 72,
    "Rohan": 30,
    "Ankit": 65
}

pass_count = 0

for name, mark in marks.items():

    # Assume 40 is the passing mark
    if mark >= 40:
        pass_count = pass_count + 1

print("Q20 - Passed students:", pass_count)


# ------------------------------------------------------------
# Q21. Create a dictionary of only passing students
# ------------------------------------------------------------

marks = {
    "Rahul": 80,
    "Amit": 45,
    "Raj": 72,
    "Rohan": 30,
    "Ankit": 65
}

passed = {}

for name, mark in marks.items():

    if mark >= 40:

        # Add passing student to new dictionary
        passed[name] = mark

print("Q21 - Passed:", passed)




# ============================================================
# IMPORTANT DICTIONARY METHODS
# ============================================================

data = {
    "name": "Rahul",
    "age": 25,
    "city": "Pune"
}


# keys()
# Returns all keys
print("keys():", data.keys())


# values()
# Returns all values
print("values():", data.values())


# items()
# Returns key-value pairs
print("items():", data.items())


# get()
# Safely gets a value
print("get():", data.get("name"))


# update()
# Adds or changes key-value pairs
data.update({"age": 26})

print("update():", data)


# pop()
# Removes a specific key
data.pop("city")

print("pop():", data)


# setdefault()
# Adds a key only if it doesn't already exist
data.setdefault("country", "India")

print("setdefault():", data)


# copy()
# Creates a copy of the dictionary
new_data = data.copy()

print("copy():", new_data)


# clear()
# Removes all key-value pairs
new_data.clear()

print("clear():", new_data)


# ============================================================
# DICTIONARY COMPREHENSION
# ============================================================


# Dictionary comprehension is a short way
# to create dictionaries using a loop.


numbers = [1, 2, 3, 4, 5]

# Create dictionary:
# key = number
# value = square

squares = {
    num: num * num
    for num in numbers
}

print("Dictionary comprehension:", squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ------------------------------------------------------------
# Dictionary comprehension with condition
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num * num
    for num in numbers
    if num % 2 == 0
}

print("Even squares:", even_squares)

# Output:
# {2: 4, 4: 16, 6: 36}


# ============================================================
# IMPORTANT: KEYS MUST BE UNIQUE
# ============================================================

student = {
    "name": "Rahul",
    "name": "Amit"
}

# The second "name" replaces the first one.
print("Duplicate key:", student)

# Output:
# {'name': 'Amit'}


# ============================================================
# DICTIONARY WITH DIFFERENT TYPES OF VALUES
# ============================================================

student = {
    "name": "Rahul",              # String
    "age": 25,                    # Integer
    "marks": 85.5,                # Float
    "passed": True,               # Boolean
    "subjects": ["Math", "SQL"],  # List
    "address": {                  # Nested dictionary
        "city": "Pune",
        "country": "India"
    }
}

print("Mixed dictionary:", student)


# ============================================================
# ACCESS NESTED DICTIONARY
# ============================================================

# Access city inside address
city = student["address"]["city"]

print("Nested city:", city)


# ============================================================
# QUICK DICTIONARY CHEAT SHEET
# ============================================================

# Create:
# student = {"name": "Rahul", "age": 25}

# Access:
# student["name"]

# Safe access:
# student.get("name")

# Add:
# student["city"] = "Pune"

# Change:
# student["age"] = 26

# Delete:
# student.pop("age")

# Keys:
# student.keys()

# Values:
# student.values()

# Key + Value:
# student.items()

# Check key:
# "name" in student

# Number of items:
# len(student)

# Update:
# student.update({"city": "Pune"})

# Copy:
# student.copy()

# Remove everything:
# student.clear()


# ============================================================
# FINAL COMPARISON
# ============================================================

# LIST
# [10, 20, 30]
# - Ordered
# - Allows duplicates
# - Mutable
# - Uses INDEX


# TUPLE
# (10, 20, 30)
# - Ordered
# - Allows duplicates
# - Immutable
# - Uses INDEX


# SET
# {10, 20, 30}
# - Unordered
# - Does NOT allow duplicates
# - Mutable
# - Does NOT use INDEX


# DICTIONARY
# {"name": "Rahul", "age": 25}
# - Stores KEY : VALUE
# - Keys must be unique
# - Mutable
# - Access using KEY