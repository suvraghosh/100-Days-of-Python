import random
# Dictionary Comprehension
names = ["Alex", "CodeWithHarry", "Dave", "Beth", "AnalysisWithGarry"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Conditional Dictionary Comprehension
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

"""You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given 
sentence and calculates the number of letters in each word."""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}
print(result)

