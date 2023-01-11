import random


def monthly_wage_calculator(full_count, part_count, count):
    print("\t\t\t\tfull days = ", full_count)
    print("\t\t\t\tpart time days = ", part_count)
    print("\t\t\t\tabsent = ", count, "\n")
    monthly_employee_attendance = full_count + part_count
    monthly_working_hours = monthly_employee_attendance * 8
    monthly_wages = wage_per_hour * monthly_working_hours
    print("Monthly wages = ", monthly_wages)


def monthly_random_check(full_count, part_count):
    count = 0
    for i in range(0,21):
        random_value = random.randint(0, 2)
        if random_value == 1:
            full_count =  full_count + 1
        elif random_value == 2:
            part_count = part_count + 1
        else:
            count = count + 1

    monthly_wage_calculator(full_count,part_count,count)


def random_check():
    random_value = random.randint(0, 2)
    if random_value == 1:
        print(random_value, "====> Employee is full_time")
        return 1
    elif random_value == 2:
        print(random_value, "====> Employee is part_time")
        return 2
    else:
        print(random_value, "====> Employee is absent")
        return 0

print("Welcome to employee wage calculator")
fullCount = 0
partCount = 0
count=0
wage_per_hour = 20
full_day_hours = 8
part_time_hours = 8
working_day_pr_month = 20
dailyWage = 20 * 8
check = random_check()
if check == 1:
    print("Full time employee --> Daily wage = ", dailyWage, "\n")
elif check == 2:
    print(" PartTime employee -->  Daily wage = ", dailyWage, "\n")
elif check == 0:
    print("Employee absent --> Daily wage = 0 \n")

monthly_random_check(fullCount,partCount)

