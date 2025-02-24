import random

class EmployeeWage:
    @staticmethod
    def compute_employee_wage(company_name, wage_per_hour, max_working_days, max_working_hours):
        total_wage = 0
        total_hours = 0
        total_days = 0

        while total_hours < max_working_hours and total_days < max_working_days:
            total_days += 1
            emp_type = random.choice(["full_time", "part_time", "absent"])

            if emp_type == "full_time":
                daily_hours = 8
            elif emp_type == "part_time":
                daily_hours = 4
            else:
                daily_hours = 0

            total_hours += daily_hours
            total_wage += daily_hours * wage_per_hour

        print(f"Total Employee Wage for {company_name}: {total_wage}")

EmployeeWage.compute_employee_wage("Company A", 25, 20, 100)
EmployeeWage.compute_employee_wage("Company B", 30, 22, 120)

