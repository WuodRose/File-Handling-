
# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is my week five\n")
        file.write("01139973\n")
        file.write("Hello, wellcom to wuodrose python platform !\n")
    print("wellcom to wuodrose python platform .")
except Exception as e:
    print(f"An error occurred: {e}")
