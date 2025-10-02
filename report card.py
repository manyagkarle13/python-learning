name = input("Enter student name: ")
Maths = int(input("Enter marks for subject 1, Maths: "))
Science = int(input("Enter marks for subject 2, Science: "))
Social = int(input("Enter marks for subject 3, Social: "))
marks = [Maths, Science, Social]
average_marks = sum(marks) / 3

if average_marks>=90:
    grade='A'
elif average_marks>=75:
    grade='B'
elif average_marks>=50:
    grade='C'
else:
    grade='Fail'

print("\n--- Report Card ---")
print("Name:", name)
print("Maths:", Maths)
print("Science:", Science)
print("Social:", Social)
print("Marks:", marks)
print("Average Marks:", average_marks)  
print("Grade:", grade)
print("-------------------")    