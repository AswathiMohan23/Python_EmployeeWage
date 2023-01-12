import random


def monthly_wage_calculator(full_count, part_count, count):
    print("\t\t\t\tfull days = ", full_count)
    print("\t\t\t\tpart time days = ", part_count)
    print("\t\t\t\tabsent = ", count)
    monthly_employee_attendance = full_count + part_count
    monthly_working_hours = monthly_employee_attendance * 8  # working hrs = 8 hrs a day
    print("\t\t\t\tMonthly working hours = ", monthly_working_hours, "\n")
    monthly_wages = wage_per_hour * monthly_working_hours
    print("Monthly wages when wage per hour is 20 ===>> ", monthly_wages)


def monthly_random_check(full_count, part_count, condition):
    count = 0
    total_working_hours = 0
    total_days = 0
    if condition == "20 days":
        for i in range(0, 21):
            random_value = random.randint(0, 2)
            if random_value == 1:
                full_count = full_count + 1
            elif random_value == 2:
                part_count = part_count + 1
            else:
                count = count + 1
        print("---------------------------- Monthly wage when a condition of 20 days is given ------------------------------------------------")
        monthly_wage_calculator(full_count, part_count, count)
    else:
        while total_working_hours < 100 or total_days <= 20:
            random_value = random.randint(0, 2)
            if random_value == 1:
                total_working_hours = total_working_hours+8
                total_days = total_days+1
                if total_working_hours >= 100:
                    total_working_hours = 100
                    break
            elif random_value == 2:
                total_working_hours=total_working_hours+8
                total_days = total_days + 1
                if total_working_hours >= 100:
                    total_working_hours = 100
                    break
            else:
                total_days = total_days + 1


        print("\n----------------------Monthly wage till a condition of total days =20 and total hours =100 hours is reached ------------------------------------\n")
        print("\t\t\t\tdays = ", total_days)
        print("\t\t\t\thours=", total_working_hours, "\n")
        monthly_wage = total_working_hours * wage_per_hour  # wage per hour =20
        print("Monthly wage when total hours of 1oo hrs and total days of 20 days are reached ===>> ", monthly_wage)


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
count = 0
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

condition1 = "20 days"
condition2 = " 100 hrs 20 days"
monthly_random_check(fullCount, partCount,condition1)
monthly_random_check(fullCount, partCount,condition2)


