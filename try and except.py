print("Enter num1:")
num1 = input()
print("Enter num2:")
num2 = input()

try:
    print("The sum of these two number is:\n", int(num1) + int(num2))

except Exception as e:
    print(e)

print("this line are very important")
