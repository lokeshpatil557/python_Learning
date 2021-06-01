a = 18
print("Enter your age: ")
age = int(input())
if age > 100:
    print("age is not possible")
elif age > a:
    print("You are Eligible")
elif age == a:
    print("You have to come for test physically")
else:
    print("You are not Eligible")
