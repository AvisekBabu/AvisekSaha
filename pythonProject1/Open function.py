Location = r"C:\Users\asaha\PycharmProjects\pythonProject1\New Text Document.txt"

#file_name = open(Location, "r")
#print(file_name.read())
#file_name.close()

with open(Location, "a") as file_name:
    print(file_name.write("\nHey how are you woman"))

with open(Location, "r") as file_name:
    print(file_name.read())

#with open(Location, "r") as file_name:
#    for line in file_name:
#        print(line)