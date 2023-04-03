import time

#initial = time.time()
#print(initial)

initial2 = time.time()
for i in range(45):
    print ("My name is Avisek")
print("For loop ran in",time.time() - initial2)

initial = time.time()
print(initial)
k = 0
while(k<45):
    print("My name is Avisek")
    k+=1
print("While loop ran in",time.time() - initial)

#initial2 = time.time()
#for i in range(45):
#    print ("My name is Avisek")
#    time.sleep(2)
#print("For loop ran in",time.time() - initial2)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)