import random

class EmployeeWage:
    wage_per_hour = 20
    full_day_hours = 8
    part_time_hours = 4
    working_days_per_month = 20
    max_hours_per_month = 100

    @classmethod
    def compute_employee_wage(cls):
        total_wage = 0
        total_hours = 0
        total_days = 0

        while total_hours < cls.max_hours_per_month and total_days < cls.working_days_per_month:
            total_days += 1
            emp_type = random.choice(["full_time", "part_time", "absent"])

            if emp_type == "full_time":
                daily_hours = cls.full_day_hours
            elif emp_type == "part_time":
                daily_hours = cls.part_time_hours
            else:
                daily_hours = 0

            total_hours += daily_hours
            total_wage += daily_hours * cls.wage_per_hour

        return total_wage

print("Total Employee Wage:", EmployeeWage.compute_employee_wage())

