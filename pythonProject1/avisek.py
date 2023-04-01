a = ("Anna","Thamudu","Akka","Chelli","Nanna","Amma")
b = [33,22,36,12,59,51]
#b.sort()
#b.reverse()
#b.append(75)
#b.pop()
#b.remove(12)
#b.insert(2,21)

"""List is immutable means changable
   Tupple is mutable means not changable"""

#Tupple
#c = (1,)

#print(c)

#Swap function
#a = 1
#b = 2

#temp=a
#a=b
#b=temp

#a,b = b,a
#print(a,b)


"""Dictionary"""
Menu={'Sayan':'Fish Fry',
      "Koushik":"Fish Cutlet",
      "Babai":"Chicken",
      "Subhojit":{"Dinner":"Non-veg","Lunch":"Veg"}}

Menu["Santosh"]="Idly" ##To add any object in Menu

del Menu["Koushik"] ##To delete any obj from dict

#print(Menu["Subhojit"]["Lunch"])
#print(Menu['Sayan'])
#print(Menu)

Chart=Menu.copy()
"""Reason behind creating Chart is a shadow of orginal dict, so if we delete something in dict then
it will delete from shadow only, instead of orginal dict"""
del Chart['Sayan']
print(Chart)

Menu.update({"Satish":"Veg"})
print(Menu)
