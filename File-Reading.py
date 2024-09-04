# File Reading and Display
try:
    with open("My-File.txt", "r") as file:
        content = file.read()
    print("File content:\n")
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
