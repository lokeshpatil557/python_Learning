def age_calculator():
    return year-age


def year_calculator(year_of_birth):
    return year_of_birth + 100


def particular_age(particular_year):
    if particular_year > birth:
        return particular_year - birth
    else:
        return "the year you inserted is before you born"


year = int(input("Enter the current year : \n"))
age = int(input("Enter your age or year of birth : \n"))

if 1 < age < 100:
    year_birth = age_calculator()
    a1 = year_calculator(year_birth)
    print(f"You will be 100 in {a1}")

elif 1950 < age < year:
    a2 = year_calculator(age)
    print(f"You will be 100 in {a2}")

elif age > year:
    print("You are not yet born")

elif age > 100 or age < 1950:
    print("You seem to be the oldest person alive")
while True:
    b = input("If you want know your age in particular year Y/N \n")
    b = b.capitalize()

    if b == "Y":
        if 1 < age < 100:
            birth = age_calculator()

        elif 1950 < age < year:
            birth = age
        p_year = int(input("Which particular year age you want to know : \n"))
        p_age = particular_age(p_year)
        print(p_age)
        break
    elif b == "N":
        break
    else:
        print("INVALID INPUT")
        continue
print("Thank you for using this AGE CALCULATOR")
