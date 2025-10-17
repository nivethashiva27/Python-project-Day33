'''# Mini Project 1: Simple Personal Info Formatter

# Asking for user details
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height (in cm): ")

# Displaying formatted output
print("\n******************************")
print("👤 PERSONAL INFORMATION")
print("******************************")
print(f"Name   : {name}")
print(f"Age    : {age} years")
print(f"Height : {height} cm")
print("******************************")
'''





'''


# Mini Project 2: Simple Bill Calculator

# Input: item details
item_name = input("Enter the item name: ")
price = float(input("Enter the price of one item: ₹"))
quantity = int(input("Enter the quantity: "))

# Constants
TAX_RATE = 0.05  # 5% tax

# Calculations
subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# Output: formatted bill
print("\n******************************")
print("🧾 SIMPLE BILL CALCULATOR")
print("******************************")
print(f"Item Name : {item_name}")
print(f"Price     : ₹{price:.2f}")
print(f"Quantity  : {quantity}")
print(f"Subtotal  : ₹{subtotal:.2f}")
print(f"Tax (5%)  : ₹{tax:.2f}")
print("------------------------------")
print(f"Total Bill: ₹{total:.2f}")
print("******************************")
print("✅ Thank you for shopping with us!")'''











# 🌟 AI Powered Python Learning Material
# All Basic Python Mini Programs in One File
'''
def print_name():
    print("\n--- Print Your Name ---")
    print("Nivetha Shiva")

def print_multiple_lines():
    print("\n--- Print Multiple Lines ---")
    print("Welcome to Python Programming!\nLet's start learning together!\nHave fun coding! 🎉")

def variable_assignment():
    print("\n--- Variable Assignment and Printing ---")
    name = "Nivetha"
    age = 20
    favorite_color = "Blue"
    print(f"Name: {name}\nAge: {age}\nFavorite Color: {favorite_color}")

def data_type_identification():
    print("\n--- Data Type Identification ---")
    name = "Nivetha"
    age = 20
    height = 5.4
    is_student = True
    print(type(name))
    print(type(age))
    print(type(height))
    print(type(is_student))

def taking_user_input():
    print("\n--- Taking User Input ---")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}! 😊")

def sum_of_two_numbers():
    print("\n--- Sum of Two Numbers ---")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum is: {num1 + num2}")

def data_type_conversion():
    print("\n--- Data Type Conversion ---")
    num = input("Enter a number: ")
    print("Before conversion:", type(num))
    num = float(num)
    print("After conversion:", type(num))

def formatted_sentence():
    print("\n--- Formatted Sentence Using f-strings ---")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    print(f"Hello {name}, you are {age} years old and live in {city}.")

def area_of_rectangle():
    print("\n--- Area of a Rectangle ---")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"The area of the rectangle is {area} square units.")

def printing_receipt():
    print("\n--- Printing a Receipt ---")
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    total = quantity * price
    print("\n********** RECEIPT **********")
    print(f"Item     : {item}")
    print(f"Quantity : {quantity}")
    print(f"Price    : ₹{price:.2f}")
    print(f"Total    : ₹{total:.2f}")
    print("*****************************")

def swap_variables():
    print("\n--- Swap Two Variables ---")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

def temperature_converter():
    print("\n--- Temperature Converter (C → F) ---")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

def simple_profile_display():
    print("\n--- Simple Profile Display ---")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    height = input("Enter your height (in cm): ")
    hobby = input("Enter your favorite hobby: ")
    print("\n********** PROFILE **********")
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Height : {height} cm")
    print(f"Hobby  : {hobby}")
    print("*****************************")

# Menu-driven program
while True:
    print("\n===============================")
    print(" PYTHON MINI PROJECT MENU")
    print("===============================")
    print("1. Print Your Name")
    print("2. Print Multiple Lines")
    print("3. Variable Assignment and Printing")
    print("4. Data Type Identification")
    print("5. Taking User Input")
    print("6. Sum of Two Numbers")
    print("7. Data Type Conversion")
    print("8. Formatted Sentence Using f-strings")
    print("9. Area of a Rectangle")
    print("10. Printing a Receipt")
    print("11. Swap Two Variables")
    print("12. Temperature Converter")
    print("13. Simple Profile Display")
    print("0. Exit")

    choice = input("\nEnter your choice (0-13): ")

    if choice == "1":
        print_name()
    elif choice == "2":
        print_multiple_lines()
    elif choice == "3":
        variable_assignment()
    elif choice == "4":
        data_type_identification()
    elif choice == "5":
        taking_user_input()
    elif choice == "6":
        sum_of_two_numbers()
    elif choice == "7":
        data_type_conversion()
    elif choice == "8":
        formatted_sentence()
    elif choice == "9":
        area_of_rectangle()
    elif choice == "10":
        printing_receipt()
    elif choice == "11":
        swap_variables()
    elif choice == "12":
        temperature_converter()
    elif choice == "13":
        simple_profile_display()
    elif choice == "0":
        print("\nThank you for using the Python Mini Project Program! 👋")
        break
    else:
        print("Invalid choice! Please try again.")'''








'''
# 🎓 Mini Project 1: Simple Student Report Card

# Taking student details as input
name = input("Enter student name: ")
student_class = input("Enter class: ")

# Taking marks for 3 subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculations
total = subject1 + subject2 + subject3
percentage = (total / 300) * 100  # assuming each subject is out of 100

# Displaying formatted report card
print("\n******************************")
print("📘 STUDENT REPORT CARD")
print("******************************")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print("------------------------------")
print(f"Subject 1  : {subject1}")
print(f"Subject 2  : {subject2}")
print(f"Subject 3  : {subject3}")
print("------------------------------")
print(f"Total Marks: {total}")
print(f"Percentage : {percentage:.2f}%")
print("******************************")

# Optional: Grade Evaluation
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 45:
    grade = "C"
else:
    grade = "F"

print(f"Grade      : {grade}")
print("******************************")
'''












'''







# 💼 Mini Project 2: Employee Salary Calculator

# Taking employee details as input
emp_name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary (₹): "))
allowances = float(input("Enter total allowances (₹): "))

# Tax and deduction calculation
tax_rate = 0.10  # 10% tax
tax = basic_salary * tax_rate

# Final salary calculation
gross_salary = basic_salary + allowances
net_salary = gross_salary - tax

# Displaying formatted salary slip
print("\n******************************")
print("💰 EMPLOYEE SALARY SLIP")
print("******************************")
print(f"Employee Name : {emp_name}")
print(f"Employee ID   : {emp_id}")
print("------------------------------")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"Allowances    : ₹{allowances:.2f}")
print(f"Tax (10%)     : ₹{tax:.2f}")
print("------------------------------")
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("******************************")
print("✅ Salary processed successfully!")'''




#''' 🧮 Mini Project: Simple Calculator

# Taking user input
'''num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

# Performing the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error! Modulus by zero."
else:
    result = "Invalid operator!"

# Displaying result
print("\n******************************")
print("🧾 SIMPLE CALCULATOR RESULT")
print("******************************")
print(f"{num1} {operator} {num2} = {result}")
print("******************************")
'''


'''
# 🎯 Mini Project: Even or Odd Number Game

# Taking input from the user
number = int(input("Enter a number: "))

# Checking even or odd
if number % 2 == 0:
    print(f"{number} is an Even number ✅")
else:
    print(f"{number} is an Odd number 🔹")
'''


'''
print("\n1️⃣ Arithmetic Operations")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b if b != 0 else 'Division by zero error!'}")
print(f"Remainder: {a % b if b != 0 else 'Division by zero error!'}")
'''

'''


print("\n2️⃣ Compare Two Numbers")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")'''



'''
# -------------------------------
# 3️⃣ Swap Two Numbers (Arithmetic)
# -------------------------------
print("\n3️⃣ Swap Two Numbers Using Arithmetic Operators")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping: First = {num1}, Second = {num2}")'''







'''
# -------------------------------
# 4️⃣ Leap Year Check
# -------------------------------
print("\n4️⃣ Leap Year Checker")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year ✅")
else:
    print(f"{year} is NOT a Leap Year ❌")'''


'''


# -------------------------------
# 5️⃣ Largest of Three Numbers
# -------------------------------
print("\n5️⃣ Largest of Three Numbers")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")
'''


'''# -------------------------------
# 6️⃣ Area of Circle
# -------------------------------
print("\n6️⃣ Area of a Circle")
radius = float(input("Enter radius: "))
area = 3.14 * (radius ** 2)
print(f"Area of circle: {area}")'''

'''
# -------------------------------
# 7️⃣ Positive, Negative, or Zero
# -------------------------------
print("\n7️⃣ Number Type Checker")
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")'''

'''
# -------------------------------
# 8️⃣ Voting Eligibility
# -------------------------------
print("\n8️⃣ Voting Eligibility Checker")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote ✅")
else:
    print("You are not eligible to vote ❌")'''

'''



# -------------------------------
# 9️⃣ Grading System
# -------------------------------
print("\n9️⃣ Grade Calculator")
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")'''




'''


# -------------------------------
# 🔟 Simple ATM Withdrawal Program
# -------------------------------
print("\n🔟 Simple ATM Program")
balance = 5000
withdraw = float(input("Enter withdrawal amount: ₹"))

if withdraw > balance:
    print("Insufficient funds ❌")
else:
    balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: ₹{balance}")'''









'''
# -------------------------------
# 1️⃣1️⃣ Divisible by Both 5 and 11
# -------------------------------
print("\n1️⃣1️⃣ Divisibility Check (5 and 11)")
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11 ✅")
else:
    print(f"{num} is NOT divisible by both 5 and 11 ❌")'''



'''
# -------------------------------
# 1️⃣2️⃣ Vowel or Consonant
# -------------------------------
print("\n1️⃣2️⃣ Vowel or Consonant Checker")
ch = input("Enter a single character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print(f"'{ch}' is a vowel.")
else:
    print(f"'{ch}' is a consonant.")'''
'''
# -------------------------------
# 1️⃣3️⃣ Even or Odd (Ternary Operator)
# -------------------------------
print("\n1️⃣3️⃣ Even or Odd (Ternary)")
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")'''






'''







# 🛍️ Mini Project: Discount Calculator for a Shopping Store

# Taking total bill amount from user
bill = float(input("Enter your total bill amount (₹): "))

# Applying discount based on conditions
if bill >= 5000:
    discount_rate = 0.20
elif bill >= 3000:
    discount_rate = 0.10
elif bill >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.00

# Calculations
discount_amount = bill * discount_rate
final_amount = bill - discount_amount

# Displaying the result
print("\n******************************")
print("🧾 SHOPPING STORE BILL")
print("******************************")
print(f"Total Bill Amount : ₹{bill:.2f}")
print(f"Discount Applied  : ₹{discount_amount:.2f}")
print(f"Final Bill Amount : ₹{final_amount:.2f}")
print("******************************")
print("✅ Thank you for shopping with us!")
'''













# 🎮 Mini Project: Rock, Paper, Scissors Game
import random

# Choices available
choices = ["rock", "paper", "scissors"]

# Take user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Computer randomly selects a choice
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a Tie! 🤝")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You Win! 🎉")
elif user_choice in choices:
    print("You Lose! 😢")
else:
    print("Invalid choice! Please choose rock, paper, or scissors.")
