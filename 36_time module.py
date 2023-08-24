import time

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

initial = time.time()

k = 0
while(k<45):
    print("Hello, World!")
    time.sleep(1)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds\n")

# initial2 = time.time()
# for i in range(1000):
#     print("Hello, World!")
# print("For loop ran in", time.time() - initial2, "Seconds")




