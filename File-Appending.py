# File Appending
try:
    with open("My-File.txt", "a") as file:
        file.write("My contact Infor.\n")
        file.write("0711220579\n")
        file.write("Wuodrose@gmail.com.\n")
    print("appended successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
