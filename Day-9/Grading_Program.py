'''You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
Write a program that converts their scores to grades.'''

student_scores={
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score >= 91 and score <= 100:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)