x = float(input("Entre the first No.: "))
y = input("Entre the operater: ")
z = float(input("Entre the Second No.: "))

if (x == 45 and z == 3 and y == "*") or (z == 45 and x == 3 and y == "*"):
    print(555)
elif (x == 56 and z == 9 and y == "+") or (z == 56 and x == 9 and y == "+"):
    print(77)
elif (x == 56 and z == 6 and y == "/"):
    print(4)
elif y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("illogical Input!!")