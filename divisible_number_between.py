n = int(input("Enter the total number of items you want to share : "))
mn = int(input("Enter the minimum number you want to divide : "))
mx = int(input("Enter the maximum number you want to divide : "))
if mn == mx:
    print("The number you inserted in minimum and maximum are equal ")

while mn != mx+1:
    if n % mn == 0:
        print(f"the {mn} is divisible by {n}")
    else:
        print(f"the {mn} is not divisible by {n}")
    mn += 1
