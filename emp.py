import random

def calculate_wages(wage_per_hour=10, max_hours=100, max_days=20): 
    total_hours = 0
    total_days = 0
    total_wages = 0

    while total_hours < max_hours and total_days < max_days:
        work_hours = random.randint(4, 8)  # Random work hours per day (4 to 8 hours)
        
        if total_hours + work_hours > max_hours:
            work_hours = max_hours - total_hours  # Adjust to not exceed max hours

        total_hours += work_hours
        total_days += 1
        daily_wage = work_hours * wage_per_hour
        total_wages += daily_wage

        print(f"Day {total_days}: Worked {work_hours} hours, Earned ${daily_wage}")

    return total_days, total_hours, total_wages



days_worked, hours_worked, wages_earned = calculate_wages(wage_per_hour=10, max_hours=100, max_days=20)

print("\nTotal Days Worked:", days_worked)
print("Total Hours Worked:", hours_worked)
print("Total Wages Earned: $", wages_earned)
