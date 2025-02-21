import random

def get_work_hours():
    work_type = random.choice(["full_time", "part_time", "absent"])
    
    switch_case = {
        "full_time": 8,
        "part_time": 4,
        "absent": 0
    }
    
    return switch_case.get(work_type, 0), work_type

def calculate_daily_wage(wage_per_hour=20):
    work_hours, work_type = get_work_hours()
    daily_wage = wage_per_hour * work_hours

    if work_type == "absent":
        return "Employee is Absent. No Wage for Today."
    return f"Employee worked {work_hours} hours ({work_type}). Daily Wage: {daily_wage}"

print(calculate_daily_wage())
