def fab(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fab(n-1)+fab(n-2)


n = int(input("enter the digit number: \n"))
print("your required Fibonacci series number is :\n", fab(n))