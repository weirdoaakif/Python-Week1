# Minor update to force track
# Day 2 - Control Flow Practice

# 1. Check if a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Check if a number is even or odd
num = int(input("Enter another number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Find largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is larger")
elif b > a:
    print(f"{b} is larger")
else:
    print("Both are equal")

# 4. Age eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")