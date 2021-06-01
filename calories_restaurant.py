cal_list = []
a = int(input("how many numbers you have inserted"))
i = 0
while i < a:
    b = input("Insert the calories in the menu ")
    cal_list.append(b)
    i += 1
print(f"the list you entered is {cal_list}")

print("This is first method")
cal_list.reverse()
print(f"the reversed list is {cal_list}")

# this is only to reverse back so that third method show the same result
cal_list.reverse()

print("This is second method")
var = cal_list[::-1]
print(f"the reversed list is {var}")

j = 0
print("This is third method")
cal_list[j], cal_list[a-j-1] = cal_list[a-j-1], cal_list[j]
print(f"the reversed list is {cal_list}")
