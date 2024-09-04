try:
    # File Creation
    with open("my-file.txt", "w") as file:
        file.write("This is my week five\n")
        file.write("01139973\n")
        file.write("Hello, welcome to Wuodrose Python platform!\n")
    print("Welcome to Wuodrose Python platform.")
    
    # File Reading
    with open("my-file.txt", "r") as file:
        content = file.read()
    print("File content:\n")
    print(content)
    
    # File Appending
    with open("my-file.txt", "a") as file:
        file.write("My contact info.\n")
        file.write("0711220579\n")
        file.write("Wuodrose@gmail.com.\n")
    print("Appended successfully.")
    
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File handling operation completed.")
