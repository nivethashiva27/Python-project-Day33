'''# Mini Project 1: Student Grade Tracker

# Empty dictionary to store student names and grades
students = {}

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[name] = grade
    print(f"{name} has been added with grade {grade}.\n")

def update_grade():
    name = input("Enter the student name to update: ")
    if name in students:
        new_grade = input("Enter the new grade: ")
        students[name] = new_grade
        print(f"{name}'s grade updated to {new_grade}.\n")
    else:
        print("Student not found!\n")

def remove_student():
    name = input("Enter the student name to remove: ")
    if name in students:
        del students[name]
        print(f"{name} has been removed.\n")
    else:
        print("Student not found!\n")

def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\n--- Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")
        print("----------------------\n")

# Main program loop
while True:
    print("===== Student Grade Tracker =====")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Display All Students")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Exiting Student Grade Tracker. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")























# Mini Project 2: To-Do List Manager

# Empty list to store tasks
todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"'{task}' has been added to your to-do list.\n")

def mark_completed():
    view_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["completed"] = True
            print(f"Task '{todo_list[task_num]['task']}' marked as completed.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def remove_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed = todo_list.pop(task_num)
            print(f"Task '{removed['task']}' has been removed.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!\n")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(todo_list, start=1):
            status = "✅ Completed" if task["completed"] else "🕓 Pending"
            print(f"{i}. {task['task']} - {status}")
        print("------------------\n")

# Main program loop
while True:
    print("===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View All Tasks")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        mark_completed()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")





















# Mini Project 3: Student Grades Management using Tuples

# Tuples storing student names and their grades
students = ("Alice", "Bob", "Charlie", "David", "Emma")
grades = (85, 92, 78, 90, 88)

# Function to display all students and grades
def display_all():
    print("\n--- Student Grades ---")
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")
    print("----------------------\n")

# Function to show grade statistics
def show_statistics():
    print("\n--- Grade Statistics ---")
    print(f"Highest Grade: {max(grades)}")
    print(f"Lowest Grade: {min(grades)}")
    print(f"Average Grade: {sum(grades) / len(grades):.2f}")
    print("------------------------\n")

# Function to access a student's grade using index
def access_by_index():
    try:
        index = int(input(f"Enter student index (0 to {len(students)-1}): "))
        if 0 <= index < len(students):
            print(f"{students[index]}'s Grade: {grades[index]}\n")
        else:
            print("Invalid index!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Main program loop
while True:
    print("===== STUDENT GRADES MANAGEMENT =====")
    print("1. View All Student Grades")
    print("2. Show Highest, Lowest, and Average Grade")
    print("3. Access Student Grade by Index")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_all()
    elif choice == "2":
        show_statistics()
    elif choice == "3":
        access_by_index()
    elif choice == "4":
        print("Exiting Student Grades Management. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")


















# Mini Project 4: Inventory Management System using Tuples

# Tuples storing item names and their quantities
items = ("Apples", "Bananas", "Oranges", "Mangoes")
quantities = (50, 30, 20, 15)

def view_inventory():
    print("\n--- Current Inventory ---")
    for i in range(len(items)):
        print(f"{items[i]}: {quantities[i]} units")
    print("-------------------------\n")

def add_item():
    global items, quantities
    new_item = input("Enter new item name: ")
    try:
        new_qty = int(input("Enter quantity: "))
        items += (new_item,)
        quantities += (new_qty,)
        print(f"{new_item} added with quantity {new_qty}.\n")
    except ValueError:
        print("Invalid quantity! Please enter a number.\n")

def access_item():
    try:
        index = int(input(f"Enter item index (0 to {len(items)-1}): "))
        if 0 <= index < len(items):
            print(f"{items[index]}: {quantities[index]} units\n")
        else:
            print("Invalid index!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def show_slice():
    try:
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("\n--- Inventory Slice ---")
        print(items[start:end])
        print(quantities[start:end])
        print("-----------------------\n")
    except ValueError:
        print("Invalid input! Please enter numbers.\n")

# Main program loop
while True:
    print("===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View All Items")
    print("2. Add New Item")
    print("3. Access Item by Index")
    print("4. View Inventory Slice")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        access_item()
    elif choice == "4":
        show_slice()
    elif choice == "5":
        print("Exiting Inventory Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
'''


# Mini Project 1: Student Management System (Using Lists)

# Empty list to store student names
'''students = []

def add_student():
    name = input("Enter Student Name: ")
    students.append(name)
    print(f"Student '{name}' added successfully!\n")

def remove_student():
    name = input("Enter Student Name to remove: ")
    if name in students:
        students.remove(name)
        print(f"Student '{name}' removed successfully!\n")
    else:
        print("Student not found!\n")

def update_student():
    old_name = input("Enter the current student name: ")
    if old_name in students:
        new_name = input("Enter the new name: ")
        index = students.index(old_name)
        students[index] = new_name
        print(f"Student name updated from '{old_name}' to '{new_name}'.\n")
    else:
        print("Student not found!\n")

def show_students():
    if not students:
        print("No students in the list.\n")
    else:
        print("Student List:", students, "\n")

# Main program loop
while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Name")
    print("4. Show All Students")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        show_students()
    elif choice == "5":
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
'''


'''# Mini Project 2: Shopping Cart System (Using Nested Lists)

# Empty list to store products and prices
cart = []

def add_product():
    product_name = input("Enter Product Name: ")
    try:
        price = float(input("Enter Price: "))
        cart.append([product_name, price])
        print(f"Product '{product_name}' added successfully!\n")
    except ValueError:
        print("Invalid price! Please enter a number.\n")

def remove_product():
    product_name = input("Enter Product Name to remove: ")
    for item in cart:
        if item[0].lower() == product_name.lower():
            cart.remove(item)
            print(f"Product '{product_name}' removed successfully!\n")
            return
    print("Product not found in cart!\n")

def view_cart():
    if not cart:
        print("Your shopping cart is empty.\n")
        return
    total_price = sum(item[1] for item in cart)
    print("\n--- Shopping Cart ---")
    for item in cart:
        print(f"{item[0]} - ₹{item[1]}")
    print("----------------------")
    print(f"Total Items: {len(cart)}")
    print(f"Total Price: ₹{total_price}\n")

def checkout():
    if not cart:
        print("Your cart is empty. Nothing to checkout!\n")
        return
    total_price = sum(item[1] for item in cart)
    print("\n===== CHECKOUT =====")
    print("Items Purchased:")
    for item in cart:
        print(f"- {item[0]}: ₹{item[1]}")
    print("--------------------")
    print(f"Total Amount: ₹{total_price}")
    print("Thank you for shopping with us! 🛍️\n")
    cart.clear()

# Main program loop
while True:
    print("===== SHOPPING CART SYSTEM =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("Exiting Shopping Cart System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
'''

'''
# Mini Project 3: Student Marks Analyzer using Tuples

# Step 1: Create a tuple containing marks of 5 subjects
marks = (85, 92, 78, 88, 90)

print("Student Marks:", marks)

# Step 2: Calculate total, highest, lowest, and average marks
total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total / len(marks)

print("\n--- Marks Analysis ---")
print(f"Total Marks: {total}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.2f}")

# Step 3: Convert tuple to list to modify a mark
marks_list = list(marks)
print("\nConverting tuple to list for modification...")
print("Current Marks List:", marks_list)

# Modify one subject mark
index_to_update = int(input("Enter the subject index to update (0-4): "))
if 0 <= index_to_update < len(marks_list):
    new_mark = int(input("Enter the new mark: "))
    marks_list[index_to_update] = new_mark
    print("Mark updated successfully!")
else:
    print("Invalid index!")

# Step 4: Convert list back to tuple
marks = tuple(marks_list)
print("\nUpdated Marks Tuple:", marks)

# Step 5: Show updated analysis
total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total / len(marks)

print("\n--- Updated Marks Analysis ---")
print(f"Total Marks: {total}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.2f}")
'''


# Mini Project 4: Shopping Cart System using Tuples

# Step 1: Create a tuple containing different product names
cart = ("Laptop", "Phone", "Headphones", "Charger", "Laptop")

def view_cart():
    print("\n--- Shopping Cart ---")
    if len(cart) == 0:
        print("Your cart is empty!")
    else:
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item}")
    print("----------------------\n")

def add_product():
    global cart
    new_product = input("Enter product name to add: ")
    cart_list = list(cart)              # Convert tuple to list
    cart_list.append(new_product)       # Add new product
    cart = tuple(cart_list)             # Convert back to tuple
    print(f"'{new_product}' added to cart successfully!\n")

def remove_product():
    global cart
    remove_item = input("Enter product name to remove: ")
    cart_list = list(cart)              # Convert tuple to list
    if remove_item in cart_list:
        cart_list.remove(remove_item)
        cart = tuple(cart_list)
        print(f"'{remove_item}' removed successfully!\n")
    else:
        print("Product not found in cart!\n")

def count_product():
    product_name = input("Enter product name to count: ")
    count = cart.count(product_name)
    print(f"'{product_name}' appears {count} time(s) in your cart.\n")

def show_first_three():
    print("\nFirst three items in the cart:")
    print(cart[:3])                     # Tuple slicing
    print()

# Main program loop
while True:
    print("===== SHOPPING CART SYSTEM (Using Tuples) =====")
    print("1. View All Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Count Product Occurrence")
    print("5. Show First Three Items")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_cart()
    elif choice == "2":
        add_product()
    elif choice == "3":
        remove_product()
    elif choice == "4":
        count_product()
    elif choice == "5":
        show_first_three()
    elif choice == "6":
        print("Exiting Shopping Cart System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
