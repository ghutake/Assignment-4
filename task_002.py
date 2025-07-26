file1 = "output.txt"
user_input = input("Enter text to write to the file: ")
with open(file1, "w") as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt.\n")

additional_input = input("Error additional text to append: ")
with open(file1, "a") as file:
    file.write(additional_input + "\n")
print("Data successfully appended.\n")

print("Final content of output.txt")
with open(file1, "r") as file:
    print(file.read())