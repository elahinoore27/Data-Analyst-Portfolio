


# A tuple is created using round brackets ()
numbers = (10, 20, 30, 40, 50)

# Print the complete tuple
print("Q1:", numbers)


favorite_food = (
    "Biryani",
    "Butter Chicken",
    "Fried Rice",
    "Pizza",
    "Burger"
)

# The loop takes one food at a time from the tuple
for food in favorite_food:
    print("Q2:", food)


numbers = (10, 20, 30, 40, 50)

# len() tells us how many items are inside the tuple
print("Q3 - Length:", len(numbers))


# ------------------------------------------------------------
# Q4. Print first, last and middle element
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

# Index starts from 0
print("Q4 - First:", numbers[0])

# -1 means the last item
print("Q4 - Last:", numbers[-1])

# Index 2 is the middle item in this 5-item tuple
print("Q4 - Middle:", numbers[2])


# ------------------------------------------------------------
# Q5. Access an item using its index
# ------------------------------------------------------------

fruits = ("apple", "banana", "mango", "orange")

# banana is at index 1
print("Q5:", fruits[1])


# ------------------------------------------------------------
# Q6. Check if an item exists
# ------------------------------------------------------------

fruits = ("apple", "banana", "mango", "orange")

# 'in' checks whether an item exists in the tuple
if "mango" in fruits:
    print("Q6: Mango is present")
else:
    print("Q6: Mango is not present")


# ------------------------------------------------------------
# Q7. Count how many times 5 appears
# ------------------------------------------------------------

numbers = (5, 2, 5, 8, 5, 10)

# count() tells us how many times a value appears
count = numbers.count(5)

print("Q7 - Number of 5s:", count)



count=0
for i in numbers:
    if i==5:
        count=count+1
print(count)



# ------------------------------------------------------------
# Q8. Find the index of orange
# ------------------------------------------------------------

fruits = ("apple", "banana", "mango", "orange")

# index() returns the position of the first matching item
index = fruits.index("orange")

print("Q8 - Orange index:", index)


# ============================================================
# LEVEL 2 - TUPLE LOGIC
# ============================================================


# ------------------------------------------------------------
# Q9. Find the sum of all numbers
# ------------------------------------------------------------

numbers = (5, 10, 15, 20, 25)

# Start the total from zero
total = 0

# Take each number from the tuple
for num in numbers:

    # Add the current number to total
    total = total + num

print("Q9 - Sum:", total)


# ------------------------------------------------------------
# Q10. Find the largest number WITHOUT max()
# ------------------------------------------------------------

numbers = (10, 25, 7, 45, 18)

# Assume the first number is the largest
largest = numbers[0]

for num in numbers:

    # If current number is greater than largest
    if num > largest:

        # Update largest
        largest = num

print("Q10 - Largest:", largest)


# ------------------------------------------------------------
# Q11. Find the smallest number WITHOUT min()
# ------------------------------------------------------------

numbers = (10, 25, 7, 45, 18)

# Assume the first number is the smallest
smallest = numbers[0]

for num in numbers:

    # If current number is smaller
    if num < smallest:

        # Update smallest
        smallest = num

print("Q11 - Smallest:", smallest)


# ------------------------------------------------------------
# Q12. Count even numbers
# ------------------------------------------------------------

numbers = (12, 7, 8, 15, 20, 33, 42)

# Start the counter at zero
count = 0

for num in numbers:

    # Even number gives remainder 0 when divided by 2
    if num % 2 == 0:

        # Increase counter by 1
        count = count + 1

print("Q12 - Even count:", count)


# ------------------------------------------------------------
# Q13. Create a tuple containing only odd numbers
# ------------------------------------------------------------

numbers = (12, 7, 8, 15, 20, 33, 42)

# Start with an empty tuple
odd_numbers = ()

for num in numbers:

    # Odd numbers give remainder 1 when divided by 2
    if num % 2 != 0:

        # Tuples don't have append()
        # So we create a new tuple using +
        #
        # (num,) is a tuple containing one item
        odd_numbers = odd_numbers + (num,)

print("Q13 - Odd numbers:", odd_numbers)


# ------------------------------------------------------------
# Q14. Reverse a tuple WITHOUT reverse()
# ------------------------------------------------------------

numbers = (1, 2, 3, 4, 5)

# Start with an empty tuple
reversed_tuple = ()

for num in numbers:

    # Put the new number at the beginning
    reversed_tuple = (num,) + reversed_tuple

print("Q14 - Reversed:", reversed_tuple)


# ------------------------------------------------------------
# Q15. Count 5 using a loop
# ------------------------------------------------------------

numbers = (5, 2, 5, 8, 5, 10, 2)

count = 0

for num in numbers:

    # Check if current number is 5
    if num == 5:

        # Increase count
        count = count + 1

print("Q15 - Number of 5s:", count)


# ------------------------------------------------------------
# Q16. Separate positive and negative numbers
# ------------------------------------------------------------

numbers = (10, -5, 8, -2, 0, 15, -7)

# Empty tuples to store the results
positive = ()
negative = ()

for num in numbers:

    # Positive means greater than zero
    if num > 0:
        positive = positive + (num,)

    # Negative means less than zero
    elif num < 0:
        negative = negative + (num,)

print("Q16 - Positive:", positive)
print("Q16 - Negative:", negative)


# ------------------------------------------------------------
# Q17. Check whether all numbers are positive
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

# We initially assume every number is positive
all_positive = True

for num in numbers:

    # If we find even one number that is zero or negative
    # then all numbers are NOT positive
    if num <= 0:

        all_positive = False

        # No need to check the remaining numbers
        break

print("Q17 - All positive:", all_positive)


# ------------------------------------------------------------
# Q18. Find the average
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

total = 0

for num in numbers:

    # Add every number
    total = total + num

# Average = total / number of items
average = total / len(numbers)

print("Q18 - Average:", average)


# ============================================================
# LEVEL 3 - INTERMEDIATE
# ============================================================


# ------------------------------------------------------------
# Q19. Remove duplicate values
# ------------------------------------------------------------

numbers = (1, 2, 2, 3, 4, 4, 5, 1)

# Empty tuple for unique values
unique = ()

for num in numbers:

    # 'not in' checks whether the number is NOT already present
    if num not in unique:

        # Add the number to our new tuple
        unique = unique + (num,)

print("Q19 - Without duplicates:", unique)




# ------------------------------------------------------------
# Q21. Find common elements between two tuples
# ------------------------------------------------------------

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

common = ()

for num in tuple1:

    # Check whether the same number exists in tuple2
    if num in tuple2:

        # Add it to the common tuple
        common = common + (num,)

print("Q21 - Common:", common)


# ------------------------------------------------------------
# Q22. Combine two tuples
# ------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# + combines two tuples
combined = tuple1 + tuple2

print("Q22 - Combined:", combined)


# ------------------------------------------------------------
# Q23. Repeat a tuple
# ------------------------------------------------------------

numbers = (1, 2, 3)

# * 3 repeats the tuple three times
repeated = numbers * 3

print("Q23 - Repeated:", repeated)


# ------------------------------------------------------------
# Q24. Convert list to tuple
# ------------------------------------------------------------

numbers_list = [10, 20, 30, 40, 50]

# tuple() converts a list into a tuple
numbers_tuple = tuple(numbers_list)

print("Q24 - Tuple:", numbers_tuple)


# ------------------------------------------------------------
# Q25. Convert tuple to list
# ------------------------------------------------------------

numbers_tuple = (10, 20, 30, 40, 50)

# list() converts a tuple into a list
numbers_list = list(numbers_tuple)

print("Q25 - List:", numbers_list)





# ------------------------------------------------------------
# Q34. Reverse a tuple using slicing
# ------------------------------------------------------------

numbers = (1, 2, 3, 4, 5)

# [::-1] means start from the end and move backwards
reversed_tuple = numbers[::-1]

print("Q34 - Reversed:", reversed_tuple)



# ============================================================
# QUICK TUPLE CHEAT SHEET
# ============================================================

# Create tuple:
# numbers = (10, 20, 30)

# Access:
# numbers[0]

# Last item:
# numbers[-1]

# Slice:
# numbers[1:3]

# Reverse:
# numbers[::-1]

# Length:
# len(numbers)

# Check item:
# 20 in numbers

# Count:
# numbers.count(20)

# Find index:
# numbers.index(20)

# Combine:
# tuple1 + tuple2

# Repeat:
# tuple1 * 3

# Tuple -> List:
# list(numbers)

# List -> Tuple:
# tuple(my_list)

# Sort:
# tuple(sorted(numbers))

# IMPORTANT:
# Tuple cannot be directly changed after creation.