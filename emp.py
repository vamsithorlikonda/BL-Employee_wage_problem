import random

def check_attendance():
    return random.randint(0, 1)  # 0 for Absent, 1 for Present

def calculate_daily_wage(wage_per_hour=20, full_day_hour=8):
    if check_attendance() == 1:
        daily_wage = wage_per_hour * full_day_hour
        return f"Employee is Present. Daily Wage: {daily_wage}"
    else:
        return "Employee is Absent. No Wage for Today."

print(calculate_daily_wage())

