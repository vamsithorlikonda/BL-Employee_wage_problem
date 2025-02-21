import random

def get_work_hours():
    work_type = random.choice(["full_time", "part_time", "absent"])
    
    if work_type == "full_time":
        return 8, "Full Time"
    elif work_type == "part_time":
        return 4, "Part Time"
    else:
        return 0, "Absent"

def calculate_daily_wage(wage_per_hour=20):
    work_hours, work_type = get_work_hours()
    daily_wage = wage_per_hour * work_hours

    if work_hours == 0:
        return 0, "Absent"
    return daily_wage, work_type

def calculate_monthly_wage(total_working_days=20, wage_per_hour=20):
    total_wage = 0
    daily_wage_records = []

    for day in range(1, total_working_days + 1):
        daily_wage, work_type = calculate_daily_wage(wage_per_hour)
        total_wage += daily_wage
        daily_wage_records.append(f"Day {day}: {work_type}, Wage: {daily_wage}")

    return total_wage, daily_wage_records

total_wage, records = calculate_monthly_wage()
print("\n".join(records))
print(f"\nTotal Wage for the Month: {total_wage}")

