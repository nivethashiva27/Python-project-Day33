'''# Mini Project 1: Word Frequency Counter

# Get input from the user
sentence = input("Enter a sentence: ")

# Convert to lowercase to make counting case-insensitive
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word frequencies
frequency = {}

# Count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display results neatly
print("\nWord Frequency Count:")
print("---------------------")
for word, count in frequency.items():
    print(f"{word}: {count}")
'''

'''# Mini Project 2: Triangle Pattern Generator

# Get input from the user
rows = int(input("Enter the number of rows for the triangle: "))

# Generate the triangle pattern
for i in range(1, rows + 1):
    print("*" * i)'''









'''

# Mini Project 3: To-Do List Manager

tasks = []  # Empty list to store tasks

print("=== TO-DO LIST MANAGER ===")
print("Options: add / view / remove / exit")

while True:
    choice = input("\nEnter your choice: ").lower()

    if choice == "add":
        task = input("Enter a new task: ").strip()
        if task == "":
            print("Task cannot be empty. Try again!")
            continue
        tasks.append(task)
        print(f"✅ '{task}' added to the list.")

    elif choice == "view":
        if not tasks:
            print("📭 No tasks in your list.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "remove":
        if not tasks:
            print("⚠️ No tasks to remove.")
            continue
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ '{removed}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "exit":
        print("👋 Exiting To-Do List Manager...")
        break

    else:
        print("❌ Invalid option! Please choose add/view/remove/exit.")

else:
    # (This will run only if while loop ends normally, not with 'break')
    print("Thanks for using the To-Do List Manager!")'''












# Mini Project 4: Simple Banking System

balance = 10000  # Starting balance

print("=== SIMPLE BANKING SYSTEM ===")
print("Options: deposit / withdraw / balance / quit")

while True:
    choice = input("\nEnter your choice: ").lower()

    if choice == "deposit":
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("⚠️ Amount must be greater than zero!")
                continue
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
            print(f"💰 Current Balance: ₹{balance}")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

    elif choice == "withdraw":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("⚠️ Amount must be greater than zero!")
                continue
            if amount > balance:
                print("❌ Insufficient balance!")
                continue
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            print(f"💰 Current Balance: ₹{balance}")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

    elif choice == "balance":
        print(f"💰 Current Balance: ₹{balance}")

    elif choice == "quit":
        print("👋 Exiting Banking System... Thank you!")
        break

    else:
        # Invalid input - just skip to next iteration using 'pass'
        print("❌ Invalid option! Please choose deposit/withdraw/balance/quit.")
        pass

else:
    # This executes only if 'break' is not used (not typical here)
    print("Session ended normally without quitting.")

