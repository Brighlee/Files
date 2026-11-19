
#Brighlee Reynoso
#Files
#11/16/26


filename = input("Enter the name of the file: ")

try:
    with open(filename, "r") as file:
        for i in range(5):
            line = file.readline()
            if line == "":
                break
            print(line, end="")

except FileNotFoundError:
    print("The file was not found."
