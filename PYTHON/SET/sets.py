# ============================================================
#                 PYTHON SET PRACTICE
# ============================================================

# A SET:
# - Stores multiple values
# - Does NOT allow duplicate values
# - Is unordered
# - Does NOT support indexing like lists/tuples
# - Is mutable (we can add/remove items)
#
# Example:
# numbers = {10, 20, 30}




# ------------------------------------------------------------
# Q1. Create a set and print it
# ------------------------------------------------------------

numbers = {10, 20, 30, 40, 50}

print("Q1 - Set:", numbers)


# ------------------------------------------------------------
# Q2. Create a set with duplicate values
# ------------------------------------------------------------

numbers = {10, 20, 20, 30, 30, 40}

# A set automatically removes duplicates
print("Q2 - Duplicates removed:", numbers)

# Output will contain:
# {10, 20, 30, 40}


# ------------------------------------------------------------
# Q3. Find the number of items in a set
# ------------------------------------------------------------

numbers = {10, 20, 30, 40, 50}

# len() tells us how many items are in the set
print("Q3 - Length:", len(numbers))


# ------------------------------------------------------------
# Q4. Check whether an item exists
# ------------------------------------------------------------

fruits = {"apple", "banana", "mango", "orange"}

# 'in' checks whether an item exists in the set
if "mango" in fruits:
    print("Q4 - Mango is present")
else:
    print("Q4 - Mango is not present")


# ------------------------------------------------------------
# Q5. Add an item to a set
# ------------------------------------------------------------

fruits = {"apple", "banana", "mango"}

# add() adds one item to the set
fruits.add("orange")

print("Q5 - After add:", fruits)


# ------------------------------------------------------------
# Q6. Add multiple items
# ------------------------------------------------------------

fruits = {"apple", "banana"}

# update() adds multiple items
fruits.update(["mango", "orange", "grapes"])

print("Q6 - After update:", fruits)


# ------------------------------------------------------------
# Q7. Remove an item
# ------------------------------------------------------------

fruits = {"apple", "banana", "mango", "orange"}

# remove() removes the specified item
fruits.remove("mango")

print("Q7 - After remove:", fruits)


# ------------------------------------------------------------
# Q8. Safely remove an item using discard()
# ------------------------------------------------------------

fruits = {"apple", "banana", "mango"}

# discard() removes the item if it exists.
# If it doesn't exist, it does NOT give an error.
fruits.discard("orange")

print("Q8 - After discard:", fruits)


# ------------------------------------------------------------
# Q9. Remove any item using pop()
# ------------------------------------------------------------

numbers = {10, 20, 30, 40}

# pop() removes one item from the set.
# Because sets are unordered, we cannot predict which item.
removed = numbers.pop()

print("Q9 - Removed item:", removed)
print("Q9 - Remaining:", numbers)


# ------------------------------------------------------------
# Q10. Remove all items using clear()
# ------------------------------------------------------------

numbers = {10, 20, 30}

# clear() removes everything from the set
numbers.clear()

print("Q10 - Empty set:", numbers)


# ============================================================
# LEVEL 2 - SET OPERATIONS
# ============================================================


# ------------------------------------------------------------
# Q11. Union of two sets
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union combines all unique elements
union = a.union(b)

print("Q11 - Union:", union)

# Same operation using |
print("Q11 - Union using |:", a | b)


# ------------------------------------------------------------
# Q12. Intersection of two sets
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Intersection gives elements common to both sets
intersection = a.intersection(b)

print("Q12 - Intersection:", intersection)

# Same operation using &
print("Q12 - Intersection using &:", a & b)


# ------------------------------------------------------------
# Q13. Difference between two sets
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# a - b gives items that are in a but NOT in b
difference = a.difference(b)

print("Q13 - a difference b:", difference)

# Same operation using -
print("Q13 - Using -:", a - b)


# ------------------------------------------------------------
# Q14. Difference in the other direction
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# b - a gives items that are in b but NOT in a
difference = b - a

print("Q14 - b difference a:", difference)


# ------------------------------------------------------------
# Q15. Symmetric difference
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Symmetric difference gives elements
# that are NOT common to both sets
result = a.symmetric_difference(b)

print("Q15 - Symmetric difference:", result)

# Same operation using ^
print("Q15 - Using ^:", a ^ b)


# ------------------------------------------------------------
# Q16. Check if one set is a subset of another
# ------------------------------------------------------------

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# a is a subset of b because
# every element of a exists in b
print("Q16 - Is a subset of b?", a.issubset(b))


# ------------------------------------------------------------
# Q17. Check if one set is a superset
# ------------------------------------------------------------

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# b is a superset of a
# because b contains all elements of a
print("Q17 - Is b superset of a?", b.issuperset(a))


# ------------------------------------------------------------
# Q18. Check whether two sets are disjoint
# ------------------------------------------------------------

a = {1, 2, 3}
b = {4, 5, 6}

# Disjoint means they have NO common elements
print("Q18 - Are sets disjoint?", a.isdisjoint(b))


# ------------------------------------------------------------
# Q19. Loop through a set
# ------------------------------------------------------------

numbers = {10, 20, 30, 40, 50}

# Loop gets one item at a time
# Remember: sets have no guaranteed order
for num in numbers:
    print("Q19:", num)


# ------------------------------------------------------------
# Q20. Find even numbers from a set
# ------------------------------------------------------------

numbers = {12, 7, 8, 15, 20, 33, 42}

even_numbers = set()

for num in numbers:

    # Even number has remainder 0 when divided by 2
    if num % 2 == 0:

        # add() adds the number to the new set
        even_numbers.add(num)

print("Q20 - Even numbers:", even_numbers)


# ------------------------------------------------------------
# Q21. Find odd numbers from a set
# ------------------------------------------------------------

numbers = {12, 7, 8, 15, 20, 33, 42}

odd_numbers = set()

for num in numbers:

    # Odd number has a remainder when divided by 2
    if num % 2 != 0:
        odd_numbers.add(num)

print("Q21 - Odd numbers:", odd_numbers)


# ============================================================
# LEVEL 3 - INTERMEDIATE SET PROBLEMS
# ============================================================


# ------------------------------------------------------------
# Q22. Remove duplicates from a list using a set
# ------------------------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5, 1]

# Converting a list to a set automatically removes duplicates
unique_numbers = set(numbers)

print("Q22 - Unique numbers:", unique_numbers)


# ------------------------------------------------------------
# Q23. Find common elements between two lists
# ------------------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Intersection gives common elements
common = set1 & set2

print("Q23 - Common elements:", common)


# ------------------------------------------------------------
# Q24. Find elements present in list1 but not list2
# ------------------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

# Difference gives items only in set1
result = set1 - set2

print("Q24 - Only in list1:", result)


# ------------------------------------------------------------
# Q25. Find elements present in either list but not both
# ------------------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

# Symmetric difference
result = set1 ^ set2

print("Q25 - Not common:", result)


# ------------------------------------------------------------
# Q26. Find unique words in a sentence
# ------------------------------------------------------------

sentence = "python is easy and python is powerful"

# split() converts the sentence into a list of words
words = sentence.split()




# Q35. Find unique elements from three sets


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {5, 6, 7, 8}

# Union combines everything
all_values = a | b | c

print("Q35 - All unique values:", all_values)


# Q36. Find values common to all three sets


a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 6}
c = {3, 4, 7, 8}

# Intersection of all three sets
common = a & b & c

print("Q36 - Common to all:", common)


# ------------------------------------------------------------
# Q37. Find values that occur in exactly one set
# ------------------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}

# Values appearing in only one set
only_one = (a - b - c) | (b - a - c) | (c - a - b)

print("Q37 - Only one set:", only_one)


# ------------------------------------------------------------
# Q38. Check whether two sets are exactly equal
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {4, 3, 2, 1}

# Order does not matter in sets
if a == b:
    print("Q38 - Sets are equal")
else:
    print("Q38 - Sets are different")


# ------------------------------------------------------------
# Q39. Find common letters in multiple words
# ------------------------------------------------------------

word1 = "python"
word2 = "typhoon"

set1 = set(word1)
set2 = set(word2)

common_letters = set1 & set2

print("Q39 - Common letters:", common_letters)


# ------------------------------------------------------------
# Q40. Find unique numbers from multiple lists
# ------------------------------------------------------------

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]

# Convert each list into a set
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Union gives every unique value
unique_values = set1 | set2 | set3

print("Q40 - Unique values:", unique_values)


# ============================================================
# IMPORTANT SET METHODS
# ============================================================

numbers = {10, 20, 30}

# add() -> add one item
numbers.add(40)
print("add():", numbers)

# update() -> add multiple items
numbers.update([50, 60])
print("update():", numbers)

# remove() -> remove an item
numbers.remove(60)
print("remove():", numbers)

# discard() -> safely remove an item
numbers.discard(100)
print("discard():", numbers)

# pop() -> removes one item
removed = numbers.pop()
print("pop() removed:", removed)

# clear() -> remove everything
numbers.clear()
print("clear():", numbers)


# ============================================================
# IMPORTANT SET OPERATIONS
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

# UNION
# Everything from both sets
print("Union:", a | b)

# INTERSECTION
# Only common values
print("Intersection:", a & b)

# DIFFERENCE
# Values in a but not b
print("Difference:", a - b)

# SYMMETRIC DIFFERENCE
# Values that are not common
print("Symmetric difference:", a ^ b)

# ============================================================
# SET COMPREHENSION
# ============================================================

# Set comprehension is a short way
# to create a set using a loop.

numbers = {1, 2, 3, 4, 5, 6}

# Get squares of numbers
squares = {num * num for num in numbers}

print("Set comprehension - Squares:", squares)





numbers = {10, 20, 30}

# This is NOT allowed:
#
# print(numbers[0])
#
# It gives:
# TypeError: 'set' object is not subscriptable


# If you need an index, convert the set into a list:

numbers_list = list(numbers)

print("Converted list:", numbers_list)
print("First item:", numbers_list[0])



# Create:
# numbers = {1, 2, 3}

# Empty set:
# empty_set = set()
#
# IMPORTANT:
# {} creates an empty DICTIONARY, not a set.

# Add one:
# numbers.add(4)

# Add multiple:
# numbers.update([5, 6])

# Remove:
# numbers.remove(4)

# Safe remove:
# numbers.discard(4)

# Remove any item:
# numbers.pop()

# Remove everything:
# numbers.clear()

# Length:
# len(numbers)

# Check item:
# 10 in numbers

# Union:
# a | b

# Intersection:
# a & b

# Difference:
# a - b

# Symmetric difference:
# a ^ b

# Subset:
# a.issubset(b)

# Superset:
# a.issuperset(b)

# Disjoint:
# a.isdisjoint(b)

# List -> Set:
# set(my_list)

# Set -> List:
# list(my_set)

# Immutable set:
# frozenset([1, 2, 3])


# ============================================================
# FINAL REMINDER
# ============================================================

# LIST:
# [1, 2, 3]
# Ordered
# Allows duplicates
# Mutable
# Supports indexing


# TUPLE:
# (1, 2, 3)
# Ordered
# Allows duplicates
# Immutable
# Supports indexing


# SET:
# {1, 2, 3}
# Unordered
# Does NOT allow duplicates
# Mutable
# Does NOT support indexing


# DICTIONARY:
# {"name": "Rahul", "age": 25}
# Stores KEY : VALUE pairs