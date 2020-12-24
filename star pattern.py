# stra pattern program
num = int(input("how many rows you want :"))
print("inter 0 or 1 ")
bool_var = input("1 for true value and 0 for false value : ")
if bool_var == "1":
    for i in range(0,num+1):
          print("*" *i)
else:
    for i in range(num,0,-1):
          print("*"* i)
