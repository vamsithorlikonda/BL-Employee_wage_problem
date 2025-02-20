
import random

def check_attendance():
    attendance = random.randint(0, 1)  # 0 for Absent, 1 for Present
    if attendance == 1:
        return "Employee is Present"
    return "Employee is Absent"

print(check_attendance())
