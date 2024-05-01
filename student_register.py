# This program will be gathering user data to write to text file using for loops.

# Create new variable to obtain input data for number of students.
no_students = int(input("How many students will you be registering?"))

# Iterating through range of number of students inputted.
for students in range(no_students):
    # For each student, user is asked to input the student ID number.
    student_id = input("Please enter the student ID number: ")
    # Creating new text file for appending to not overwrite previous inputted data.
    with open('reg_form.txt', 'a') as file:
        # Writing each ID number to file + dotted line for signature, followed by newline\ for readability
        file.write(student_id + '.......'+'\n')

# Opening recently created file for reading only.
with open('reg_form.txt', 'r') as file:
    lines = file.readlines()
    print(lines)        
