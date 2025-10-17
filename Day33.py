'''# 🎓 Student Grades Analyzer

# Step 1: Input number of students
num_students = int(input("Enter the number of students: "))

# Step 2: Create a dictionary to store student names and marks
students = {}

for i in range(num_students):
    name = input(f"\nEnter name of student {i + 1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Step 3: Calculate average marks
average_marks = sum(students.values()) / num_students

# Step 4: Find top-performing students
top_score = max(students.values())
top_students = [name for name, mark in students.items() if mark == top_score]

# Step 5: Display results
print("\n===== Student Grades Report =====")
for name, mark in students.items():
    print(f"{name}: {mark}")

print(f"\nAverage Marks: {average_marks:.2f}")
print(f"Top Score: {top_score}")
print("Top Performing Student(s):", ", ".join(top_students))'''








'''
# 🔺 Number Pyramid Generator

while True:
    rows = int(input("Enter the number of rows (negative number to stop): "))

    # Stop if user enters a negative number
    if rows < 0:
        print("Program stopped. Goodbye!")
        break

    print("\nNumber Pyramid:")
    for i in range(1, rows + 1):
        # Print spaces for alignment
        print(" " * (rows - i), end="")
        # Print numbers for each row
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to next line

    print("\n")  # Add space before next pyramid
'''














'''
# 💳 ATM PIN Verification System

# Predefined correct PIN
correct_pin = "1234"

# Allow the user 3 attempts
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")

    # Check if PIN matches
    if entered_pin == correct_pin:
        print("✅ Access Granted! Welcome to your account.")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. {attempts} attempt(s) left.\n")

else:
    # This else block runs only if the loop finishes without a break
    print("🚫 Access Denied! Your card has been blocked due to 3 incorrect attempts.")
'''












'''
# 🎲 Number Guessing Game
import random

# Step 1: Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Step 2: Set number of attempts
attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")
print("You have 5 attempts to guess it.\n")

# Step 3: Loop for guessing
for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess → "))

    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it right. The number was {secret_number}.")
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.\n")
    else:
        print("Too high! Try a lower number.\n")

else:
    # Runs if the loop completes without a correct guess
    print(f"😢 Sorry! You've used all your attempts.")
    print(f"The correct number was {secret_number}.")'''

'''




# ===========================
# 🐍 PYTHON LOOP PRACTICE PROGRAMS
# ===========================

# 1. Print each character of "PYTHON"
print("\n1. Each character of 'PYTHON':")
for ch in "PYTHON":
    print(ch)

# 2. Count vowels in a string
print("\n2. Count vowels in a string:")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

# 3. Reverse a string
print("\n3. Reverse a string:")
word = input("Enter a string to reverse: ")
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word
print("Reversed string:", reversed_word)

# 4. Print numbers 1 to 20
print("\n4. Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print()

# 5. Print even numbers from 2 to 50
print("\n5. Even numbers from 2 to 50:")
for i in range(2, 51, 2):
    print(i, end=" ")
print()

# 6. Reverse order from 10 to 1
print("\n6. Numbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 7. Enter numbers until 0 using break
print("\n7. Enter numbers until 0:")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break

# 8. Skip multiples of 5
print("\n8. Skip multiples of 5 from 1 to 50:")
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print()
'''
'''# 9. Use pass when number is 5
print("\n9. Pass example:")
for i in range(1, 11):
    if i == 5:
        pass
    print(i, end=" ")
print()

# 10. Loop with else
print("\n10. For loop with else:")
for i in range(1, 11):
    print(i, end=" ")
else:
    print("\nLoop finished successfully.")

# 11. Print characters of 'HELLO' with index
print("\n11. Characters of 'HELLO' with index:")
for index, ch in enumerate("HELLO"):
    print(f"Index {index}: {ch}")

# 12. Print words with position using enumerate
print("\n12. Print each word with position:")
sentence = input("Enter a sentence: ")
for index, word in enumerate(sentence.split(), start=1):
    print(f"Word {index}: {word}")
'''
'''# 13. Multiplication table 1 to 10 (nested loop)
print("\n13. Multiplication Table (1 to 10):")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 15)

# 14. Infinite loop printing Hello World
# ⚠️ Uncomment to test
# while True:
#     print("Hello, World!")

# 15. Infinite loop stops after 5 seconds
import time
print("\n15. Hello World for 5 seconds:")
start_time = time.time()
while True:
    print("Hello, World!")
    if time.time() - start_time > 5:
        break

# 16. Infinite input loop, break on 'exit'
print("\n16. Infinite input loop:")
while True:
    text = input("Enter something (type 'exit' to stop): ")
    if text.lower() == "exit":
        break
    print("You entered:", text)'''

# 17. Even numbers using while + continue
print("\n17. Even numbers (1 to 20) using while + continue:")
i = 0
while i < 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

# 18. Ask until positive number
print("\n18. Ask until positive number:")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative ignored.")
        continue
    print("Positive number entered:", num)
    break

# 19. Numbers except multiples of 3
print("\n19. Numbers 1–30 except multiples of 3:")
i = 1
while i <= 30:
    if i % 3 != 0:
        print(i, end=" ")
    i += 1
print()

# 20. Number guessing game (1–10)
print("\n20. Number Guessing Game:")
import random
secret = random.randint(1, 10)
while True:
    guess = int(input("Guess a number (1–10): "))
    if guess == secret:
        print("🎉 Correct! You guessed it!")
        break
    else:
        print("Try again!")

# 21. Password check loop
print("\n21. Password check:")
correct_password = "python123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("✅ Access Granted.")
        break
    else:
        print("❌ Wrong password.")

# 22. ATM system with 3 attempts
print("\n22. ATM PIN Verification:")
correct_pin = "1234"
attempts = 3
while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("✅ Access Granted!")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. {attempts} attempts left.")
else:
    print("🚫 Account Locked!")

# 23. Loop with pass (10 times)
print("\n23. Loop with pass:")
for i in range(10):
    pass
print("Loop executed 10 times (no action).")

# 24. Placeholder loop (using pass)
print("\n24. Placeholder loop:")
for i in range(5):
    pass
print("Loop ready for future code.")

# 25. While loop with else
print("\n25. While loop with else:")
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully!")

# 26. Word check for 'Python'
print("\n26. Word check for 'Python':")
while True:
    word = input("Enter a word: ")
    if word == "Python":
        print("✅ You entered 'Python'!")
        break
else:
    print("You never entered 'Python'!")

