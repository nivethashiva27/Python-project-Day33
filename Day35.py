'''# Global variable to count total transactions
total_transactions = 0

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        global total_transactions
        self.balance += amount
        total_transactions += 1
        print(f"Deposited: {amount}")

    # Withdraw method with inner function and lambda transaction fee
    def withdraw(self, amount):
        global total_transactions

        # Inner function to check if withdrawal is possible
        def can_withdraw():
            return self.balance >= amount

        # Lambda function for transaction fee (2%)
        transaction_fee = (lambda amt: amt * 0.02)(amount)

        if can_withdraw():
            self.balance -= (amount + transaction_fee)
            total_transactions += 1
            print(f"Withdrawn: {amount}")
            print(f"Transaction Fee: {transaction_fee}")
        else:
            print("Insufficient funds!")

    # Method to get balance
    def get_balance(self):
        print(f"Balance: {self.balance}")
        return self.balance


# Function demonstrating first-class function (applying interest)
def apply_interest(balance, interest_function):
    return interest_function(balance)


# Example usage
account = BankAccount("Alice", 0)
print(f"Account Holder: {account.name}")

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Show balance
account.get_balance()

# Apply 5% interest using first-class function
interest_rate = lambda bal: bal * 1.05
new_balance = apply_interest(account.get_balance(), interest_rate)
print(f"Balance after applying 5% interest: {new_balance}")

# Show total transactions (global variable)
print(f"Total Transactions: {total_transactions}")'''




from functools import reduce

# Function to calculate average using *args
def calculate_average(*args):
    return sum(args) / len(args)

# Function to assign grades using lambda + map()
def assign_grades(marks):
    return list(map(lambda m: "A" if m >= 90 else "B" if m >= 80 else "C" if m >= 70 else "F", marks))

# Function to filter passed students (grade not 'F')
def filter_passed(students):
    return list(filter(lambda s: s["grade"] != "F", students))

# Function to find highest score using reduce()
def find_highest_score(all_marks):
    return reduce(lambda a, b: a if a > b else b, all_marks)

# Recursive function to print first n student details
def print_students_recursive(students, n):
    if n == 0:
        return
    student = students[n - 1]
    print(f"Student: {student['name']}, Age: {student['age']}, Average Score: {student['average']}, Grade: {student['grade']}")
    print_students_recursive(students, n - 1)

# Function to create student dynamically using **kwargs
def create_student(**kwargs):
    return kwargs

'''
# ----------------------------
# Example Usage
# ----------------------------
students_data = []

# Student 1
marks_john = [85, 90, 80]
avg_john = calculate_average(*marks_john)
grade_john = assign_grades([avg_john])[0]
students_data.append(create_student(name="John", age=16, average=avg_john, grade=grade_john))

# Student 2
marks_emily = [92, 88, 95]
avg_emily = calculate_average(*marks_emily)
grade_emily = assign_grades([avg_emily])[0]
students_data.append(create_student(name="Emily", age=17, average=avg_emily, grade=grade_emily))

# Student 3
marks_mike = [60, 65, 58]
avg_mike = calculate_average(*marks_mike)
grade_mike = assign_grades([avg_mike])[0]
students_data.append(create_student(name="Mike", age=16, average=avg_mike, grade=grade_mike))

# Print student details using recursion
print("=== Student Details ===")
print_students_recursive(students_data, len(students_data))

# Filter passed students
passed_students = filter_passed(students_data)
passed_names = [s["name"] for s in passed_students]
print("\nPassed Students:", passed_names)

# Find highest score among all marks
all_marks = marks_john + marks_emily + marks_mike
highest = find_highest_score(all_marks)
print("Highest Score:", highest)'''














'''
# 1️⃣ Define a function greet_user()
def greet_user():
    print("Hello, User!")

greet_user()

# 2️⃣ Function to calculate sum
def calculate_sum(a, b):
    return a + b

print("Sum:", calculate_sum(5, 10))

# 3️⃣ Function to check if number is positive
def check_positive(num):
    if num > 0:
        return "Positive"
    else:
        pass

print("Check Positive:", check_positive(7))

# 4️⃣ Function to find maximum among three numbers
def find_max(a, b, c):
    return max(a, b, c)

print("Maximum:", find_max(12, 45, 30))

# 5️⃣ Demonstrate global and local variable
count = 10  # Global variable

def modify_count():
    global count
    count += 5
    print("Inside function, count =", count)

modify_count()
print("Outside function, count =", count)

# 6️⃣ Demonstrate local vs global scope
message = "Global Scope"

def modify_variable():
    message = "Local Scope"
    print("Inside function:", message)

modify_variable()
print("Outside function:", message)

# 7️⃣ Recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 8️⃣ Recursive Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("5th Fibonacci number:", fibonacci(5))

# 9️⃣ Function with *args
def sum_numbers(*args):
    return sum(args)

print("Sum of numbers:", sum_numbers(2, 4, 6, 8))

# 🔟 Function with **kwargs
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

print_student_details(name="Alice", age=16, grade="A")

# 1️⃣1️⃣ First-class function example
def apply_operation(func, a, b):
    return func(a, b)

result = apply_operation(lambda x, y: x + y, 10, 20)
print("Lambda sum result:", result)

# 1️⃣2️⃣ Outer and Inner function
def outer_function():
    def inner():
        return "Hello from Inner Function"
    return inner()

print(outer_function())

# 1️⃣3️⃣ Use map() to double each element of a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled List:", doubled)
'''















'''
class ToDoList:
    def __init__(self):
        self.tasks = []  # Initialize empty task list

    # Add a new task
    def add_task(self, task):
        self.tasks.append(task)
        print(f"✅ '{task}' added successfully!")

    # Remove a task using lambda + filter
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks = list(filter(lambda t: t != task, self.tasks))
            print(f"❌ '{task}' removed successfully!")
        else:
            print(f"⚠️ '{task}' not found in the list!")

    # Display all tasks
    def show_tasks(self):
        if not self.tasks:
            print("📋 No tasks available.")
        else:
            print("\n📝 Your Tasks:")
            list(map(lambda t: print(f"- {t}"), self.tasks))

    # Recursive menu system
    def manage_list(self):
        def menu():
            print("\n===== TO-DO LIST MANAGER =====")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Show Tasks")
            print("4. Exit")
            return input("👉 Choose an option (1-4): ")

        def process_choice(choice):
            if choice == '1':
                task = input("Enter task to add: ")
                self.add_task(task)
            elif choice == '2':
                task = input("Enter task to remove: ")
                self.remove_task(task)
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                print("👋 Exiting To-Do List... Goodbye!")
                return
            else:
                print("⚠️ Invalid choice, try again!")

            # Recursive call to continue until user exits
            self.manage_list()

        # Start recursion
        process_choice(menu())


# Run To-Do List Manager
if __name__ == "__main__":
    todo = ToDoList()
    todo.manage_list()'''



from functools import reduce

class Student:
    # Class variable to hold all student records
    students_list = []

    # Constructor
    def __init__(self, name, age, *scores):
        self.name = name       # Instance variable
        self.age = age
        self.scores = scores
        Student.students_list.append(self)  # Add to global list

    # Method to calculate average score
    def get_average(self):
        return sum(self.scores) / len(self.scores)

    # Static method to filter passing students (average >= 50)
    @staticmethod
    def filter_passing_students():
        return list(filter(lambda s: s.get_average() >= 50, Student.students_list))

    # Static method to find the student with the highest average score
    @staticmethod
    def get_highest_score():
        return reduce(lambda x, y: x if x.get_average() > y.get_average() else y, Student.students_list)

    # Static method to display all students
    @staticmethod
    def display_students():
        print("=== Student Details ===")
        for student in Student.students_list:
            print(f"Name: {student.name}, Age: {student.age}, Avg Score: {student.get_average():.2f}")


# -----------------------------
# Add Student Records
# -----------------------------
s1 = Student("Alice", 20, 45, 78, 90)
s2 = Student("Bob", 21, 88, 92, 85)
s3 = Student("Charlie", 22, 40, 35, 30)

# -----------------------------
# Display All Students
# -----------------------------
Student.display_students()

# -----------------------------
# Filter and Display Passing Students
# -----------------------------
passing_students = Student.filter_passing_students()
print("\n=== Passing Students ===")
for student in passing_students:
    print(student.name)

# -----------------------------
# Find and Display Top Student
# -----------------------------
top_student = Student.get_highest_score()
print(f"\n🏆 Top Student: {top_student.name} with Avg Score: {top_student.get_average():.2f}")
