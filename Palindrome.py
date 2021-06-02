b = int(input("how many turns you want"))
# to check whether the number is palindrome or not
for i in range(b):
    a = int(input("Enter the number : "))
    d = a
    while True:
        c = str(a)
        if c == c[:: -1]:
            if int(c) == d:
                print(f"{c} is palindrome")
                break
            else:
                print(f"the next palindrome {c}")
                break
        else:
            a += 1
            continue
