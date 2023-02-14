
"""You are going to write a List Comprehension to create a new list called result.
This new list should only contain the even numbers from the list numbers."""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [even_numbers for even_numbers in numbers if even_numbers % 2 == 0]
print(result)
