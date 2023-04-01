Location = r"C:\Dropbox\Avisek\New folder\Diag.txt"

#file_name = open(Location, "r")
#print(file_name.read())
#file_name.close()

with open(Location, "r+") as file_name:
    print(file_name.replace("\n0:-15:-1"))

#with open(Location, "r") as file_name:
#    print(file_name.read())

#with open(Location, "r") as file_name:
#    for line in file_name:
#        print(line)

