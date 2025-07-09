# Day 2 - Loops Practice

# 1. Print numbers 1 to 10 using while loop
count = 1
while count <= 10:
    print(count)
    count += 1

# 2. Sum of first n numbers
n = int(input("Enter a number: "))
sum_result = 0
i = 1
while i <= n:
    sum_result += i
    i += 1
print("Sum is:", sum_result)

# 3. Multiplication table
num = int(input("Enter number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")

# 4. Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)

# 5. Print each letter of a string
word = input("Enter a word: ")
for letter in word:
    print(letter)