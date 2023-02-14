
# List comprehension
new_numbers = [item * 2 for item in range(1, 5)]
print(new_numbers)

# List comprehension using letters
list_name = "Harry"
new_letter = [letter for letter in list_name]
print(new_letter)

# Conditional List Comprehension
names = ["Alex", "CodeWithHarry", "Dave", "Beth", "AnalysisWithGarry"]
short_names = [n for n in names if len(n) < 5]
long_names = [n.upper() for n in names if len(n) > 5]
print(short_names)
print(long_names)

"""You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain 
every number in the list numbers but each number should be squared."""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [square * square for square in numbers]
print(squared_numbers)
