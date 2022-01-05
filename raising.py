try:
    a=int(input("enter the positive number :"))
    if(a<=0):
        raise ValueError("That is not positive number!")
except ValueError as ve:
    print(ve)
