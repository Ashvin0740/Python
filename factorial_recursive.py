def factorial_recursive(n):
    if n == 1:
        return 1
    else :
        return n*factorial_recursive(n-1)

number = int(input("Enter the number:"))
print(factorial_recursive(number))