# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))
# line 28
grades = [exam_one,exam_two,exam_three]  #Itbc there was no commas between the exams.
sum = 0
for grade in grades:
  sum = sum + grade
# line 33
avg = sum / len(grades)                   #Itbc  it was len(grdes) which is not a variable.
# line 37
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:                #Itbc there was no " : " after 90 in the elif.
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))  #Itbc there was no proper brackets for letter_grade
#line 51
if letter_grade == "F":
    print("Student is failing.")         #Itbc there was no proper brackets for print
else:
    print("Student is passing.")         #Itbc there was no proper brackets for print
#line 54 and 56
