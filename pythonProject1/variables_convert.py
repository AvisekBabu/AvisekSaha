#Variables convertion
#print("Enter your first number")
#var1=input()
#print("Enter your second number")
#var2=input()

#print(type(var1))
#print("You have won",float(var1)+float(var2), "lakhs")

"""String
Functions https://www.w3schools.com/python/python_ref_string.asp"""

#String slicing
mystr="breakfast iyunda is is is"
print(len(mystr))
#print(mystr[::-2])
#print(mystr.isalnum())  ## alphanumrical word, if any gap b/w strings then "False" will print
#print(mystr.isalpha()) ## alphanumrical  word, if any gap b/w strings then "False" will print
#print(mystr.endswith("yunda")) ## Last string should match for True value
#print(mystr.count("s")) ##will print "s" count in string
#print(mystr.capitalize()) ##First word will convert into capital latter
print(mystr.upper()) ##String will convert into Capital latters
print(mystr.lower()) ##String will convert into Lower latters
print(mystr.replace("is","are")) ##String word will be replace