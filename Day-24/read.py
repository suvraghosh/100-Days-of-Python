# To read the text file

"""

text = open("Turtle.text")
read_txt_file = text.read()
print(read_txt_file)
text.close()

"""

# Another method to read the file (Here we don't need to close the file).

with open("Turtle.text") as file:
    read_text_file = file.read()
    print(read_text_file)


# The mode is by default set as read("r")

with open("Turtle.text", mode="w") as file:
    file.write("\nThere are several modules in python")

with open("new_file.text", mode="w") as file:
    file.write("new file will be created if the file is not exist")


# Absolute File Path to access the file(this is always associated with root)

with open("/Users/Lenovo/OneDrive/Desktop/my_file.text") as file:
    contents = file.read()
    print(contents)

# Relative File Path to access the file(it's depend on the current working directory)

with open("../../../Desktop/my_file.text") as file:
    contents = file.read()
    print(contents)
