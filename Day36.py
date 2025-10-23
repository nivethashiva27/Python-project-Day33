'''# Mini Project 1: Student Profile Card Generator

# Taking input from the user
name = input("Enter Student Name: ").strip().title()
age = input("Enter Age: ").strip()
course = input("Enter Course Name: ").strip().title()
university = input("Enter University Name: ").strip().title()

# Generating formatted profile
profile = f"""
🎓 STUDENT PROFILE CARD 🎓
----------------------------------
Name       : {name}
Age        : {age}
Course     : {course}
University : {university}
----------------------------------
Note: Keep working hard and learning new things!
"""

# Printing the formatted student profile
print(profile)
'''

'''# Mini Project 2: Fun String Manipulator Tool

# Taking user input
sentence = input("Enter a sentence: ").strip()

# Performing string manipulations
uppercase = sentence.upper()
lowercase = sentence.lower()
first_char = sentence[0]
last_char = sentence[-1]
reversed_sentence = sentence[::-1]
repeated_sentence = sentence * 3

# Formatting a new string
formatted_output = f"Learning {sentence.split()[0]} is really FUN!"

# Displaying results
result = f"""
✨ Fun String Manipulator ✨
----------------------------
Original Sentence : {sentence}
Uppercase          : {uppercase}
Lowercase          : {lowercase}
First Character    : {first_char}
Last Character     : {last_char}
Reversed Sentence  : {reversed_sentence}
Repeated Sentence  : {repeated_sentence}
Formatted Output   : {formatted_output}
----------------------------
"""

print(result)
'''

'''
# Mini Project 1: User Profile Formatter

# Taking user input
full_name = input("Enter your full name: ").strip().title()
age = str(input("Enter your age: ")).strip()
favorite_quote = input("Enter your favorite quote: ").strip().upper()

# Displaying the formatted output
print("\nUser Profile:")
print("-------------------------")
print(f"Name           : {full_name}")
print(f"Age            : {age}")
print(f'Favorite Quote : "{favorite_quote}"')'''





# Mini Project 2: Simple Password Generator

# Taking user input
first_name = input("Enter your First Name: ").strip()
last_name = input("Enter your Last Name: ").strip()
keyword = input("Enter your Secret Keyword: ").strip()

# Using string slicing and manipulation
part1 = first_name[:3]              # First 3 letters of first name
part2 = last_name[-3:]              # Last 3 letters of last name
part3 = keyword[::-1]               # Reversed keyword

# Concatenating and creating password
raw_password = part1 + part2 + part3
password = raw_password.title()     # Mix of uppercase and lowercase

# Displaying the generated password
print("\n🔐 Simple Password Generator 🔐")
print("-------------------------------")
print(f"First Name Part   : {part1}")
print(f"Last Name Part    : {part2}")
print(f"Reversed Keyword  : {part3}")
print(f"Generated Password : {password}")
print("-------------------------------")

