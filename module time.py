import  time
initial1 = time.time()
k = 0
while(k<50):
     print("my name is ashvin")
     # it's use to stope your program to 2 second
     # after 2second print "my name is ashvin"
     time.sleep(2)
     k+=1
print("for loop ran in", time.time() - initial1, "second")
initial2 = time.time()
for item in range(50):
     print("my self ashvin vanol")
print("for loop ran in", time.time() - initial2, "second")


# this is use to find local time
# Thu Aug  6 17:51:30 2020
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)