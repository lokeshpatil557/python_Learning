a=int(input("Enter the number"))
b=int(input("Enter the boolean number 0 or 1" ))
if b==1:
    for x in range(0,a+1):
        print(int(x)*'*')
elif b==0:
    for x in range(a,0,-1):
        print(int(x)*'*')