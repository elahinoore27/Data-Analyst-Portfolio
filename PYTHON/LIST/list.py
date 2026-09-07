n=[1,2,3,4,5]
print(n)
fav_food=["Biryani","Butter chicken","Fried Rice","Pizza","Burger"]
for i in fav_food:
    print(i)
print(len(n))
print(len(fav_food))

numbers=[10,20,30,40,50]
print(numbers[0])
print(numbers[-1])
print(numbers[2])

fruits=["apple","banana","Mango","Orange"]
fruits[1]="Grapes"
print(fruits)
fruits.append("Watermealon")
print(fruits)
fruits.insert(1,"Kiwi")
print(fruits)

fruits.remove("Mango")
print(fruits)




# 9. Find the sum of all numbers

numbers = [5, 10, 15, 20, 25]

total = 0  # Variable to store the sum

for num in numbers:
    total = total + num  # Add each number to total

print("Q9 - Sum:", total)



# 10. Find the largest number without max()

numbers = [10, 25, 7, 45, 18]

largest = numbers[0]  # Assume first number is the largest

for num in numbers:
    if num > largest:  # Check if current number is bigger
        largest = num  # Update largest number

print("Q10 - Largest:", largest)


# 11. Find the smallest number without min()


numbers = [10, 25, 7, 45, 18]

smallest = numbers[0]  # Assume first number is the smallest

for num in numbers:
    if num < smallest:  # Check if current number is smaller
        smallest = num  # Update smallest number

print("Q11 - Smallest:", smallest)


# 12. Count how many even numbers are present

numbers = [12, 7, 8, 15, 20, 33, 42]

count = 0  # Variable to count even numbers

for num in numbers:
    if num % 2 == 0:  # If remainder is 0, number is even
        count = count + 1  # Increase the count

print("Q12 - Even numbers:", count)
# Output: Q12 - Even numbers: 4

#print even number
numbers = [12, 7, 8, 15, 20, 33, 42]
for num in numbers:
    if num%2==0:
        print(num) #direct print all even numner 

# 13. Create a new list containing odd numbers

numbers = [12, 7, 8, 15, 20, 33, 42]

odd_numbers = []  # Empty list to store odd numbers

for num in numbers:
    if num % 2 != 0:  # Check if number is odd
        odd_numbers.append(num)  # Add number to new list

print("Q13 - Odd numbers:", odd_numbers)
# Output: Q13 - Odd numbers: [7, 15, 33]


# 14. Reverse a list without using reverse()

numbers = [1, 2, 3, 4, 5]

reversed_list = []  # Empty list for reversed values

for num in numbers:
    # Insert each number at index 0
    # This moves previous values to the right
    reversed_list.insert(0, num)

print("Q14 - Reversed list:", reversed_list)
# Output: Q14 - Reversed list: [5, 4, 3, 2, 1]


# --------------------------------------------
# 15. Count how many times 5 appears
# --------------------------------------------

numbers = [5, 2, 5, 8, 5, 10, 2]

count = 0  # Variable to count occurrences of 5

for num in numbers:
    if num == 5:  # Check if current number is 5
        count = count + 1  # Increase the count

print("Q15 - Number of 5s:", count)
# Output: Q15 - Number of 5s: 3



# ------------------------------------------------------------
# 16. Remove duplicate values
# ------------------------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique_numbers = []  # Empty list to store unique values

for num in numbers:
    # Check if the number is not already in the new list
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Q16 - Without duplicates:", unique_numbers)

# Output:
# [1, 2, 3, 4, 5]



# ------------------------------------------------------------
# 18. Separate positive and negative numbers
# ------------------------------------------------------------

numbers = [10, -5, 8, -2, 0, 15, -7]

positive_numbers = []  # List for positive numbers
negative_numbers = []  # List for negative numbers

for num in numbers:

    if num > 0:
        positive_numbers.append(num)

    elif num < 0:
        negative_numbers.append(num)

print("Q18 - Positive numbers:", positive_numbers)
print("Q18 - Negative numbers:", negative_numbers)

# Output:
# Positive numbers: [10, 8, 15]
# Negative numbers: [-5, -2, -7]


# ------------------------------------------------------------
# 19. Find names whose length is greater than 4
# ------------------------------------------------------------

names = ["Rahul", "Amit", "Raj", "Ankit", "Rohan"]

long_names = []  # Empty list for names longer than 4 characters

for name in names:

    # len() gives the number of characters
    if len(name) > 4:
        long_names.append(name)

print("Q19 - Names longer than 4:", long_names)

# Output:
# ['Rahul', 'Ankit', 'Rohan']


# ------------------------------------------------------------
# 20. Find common elements between two lists
# ------------------------------------------------------------

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

common = []  # List to store common elements

for num in a:

    # Check whether the number exists in list b
    if num in b:
        common.append(num)

print("Q20 - Common elements:", common)

# Output:
# [3, 4, 5]
