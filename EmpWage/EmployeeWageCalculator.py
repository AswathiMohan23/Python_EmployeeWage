import random


def random_check():
    random_value = random.randint(0, 1)
    if random_value == 1:
        print(random_value, "====> Employee is present")
        return 1
    else:
        print(random_value, "====> Employee is absent")
        return 0


print("Welcome to employee wage calculator")
wage_per_hour = 20
full_day_hour = 8
if random_check() == 1:
    dailyWage = 20 * 8
    print("Daily wage = ", dailyWage)
else:
    print("Daily wage = 0 ")



