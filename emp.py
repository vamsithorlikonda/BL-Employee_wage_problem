import random

def get_work_hours():
    return random.choice([4, 8])

def calculate_daily_wage(wage_per_hour=20):
    work_hours = get_work_hours()
    daily_wage = wage_per_hour * work_hours
    return f"Worked {work_hours} hours. Daily Wage: {daily_wage}"

print(calculate_daily_wage())
