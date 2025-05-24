from datetime import datetime, timedelta
import calendar, questionary
from pyfiglet import Figlet

# Constants (default values if not taken from user input)

f = Figlet()
print(f.renderText('SALARY CALCULATOR'))
print("This tool calculates your salary based on your monthly pay, working days per week, and hours worked per day.")
print("⚠️ Warning: This calculator uses the actual number of working days in each month (based on your selected working days per week) to calculate salary proration and leave deductions. **Leave deductions are now based on your actual eligible working days for that month, not a fixed divisor.** Results may differ from calculations that use a fixed divisor (such as 30 or 26 days). Always check your company’s payroll policy for the official method. \n\n")


def count_working_days(year: int, month: int, working_days_per_week: int) -> int:
    weekdays = set(range(5 if working_days_per_week == 5 else 6))  # Mon–Fri or Mon–Sat
    total_days = calendar.monthrange(year, month)[1]
    return sum(1 for day in range(1, total_days + 1)
               if datetime(year, month, day).weekday() in weekdays)

def calculate_hourly_wage(monthly_pay: float, working_days_per_week: int, hours_per_day: float) -> float:
    avg_working_days = 22 if working_days_per_week == 6 else 20
    total_hours = avg_working_days * hours_per_day
    return monthly_pay / total_hours

def get_valid_int_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"  ❌ Invalid. Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("  ❌ Please enter a valid number.")

def main():
    try:
        # User Inputs with Validation
        monthly_pay = float(input("Enter your monthly pay (in ₹): "))
        working_days_per_week = get_valid_int_input("Enter the number of working days per week (e.g., 5 or 6): ", 1, 6)
        hours_per_day = get_valid_int_input("Enter hours worked per day (1–24): ", 1, 24)

        print(f"\nMonthly Pay: ₹{monthly_pay}")
        print(f"Working Days/Week: {working_days_per_week}")
        print(f"Hours Per Day: {hours_per_day}")

        join_date_str = input("Enter your joining date (DD-MM-YYYY): ")
        join_date = datetime.strptime(join_date_str, "%d-%m-%Y")
        today = datetime.today()

        try:
            show_monthly = questionary.select(
                "Do you want to see monthly salary breakdowns?",
                choices=["Yes", "No"]
            ).ask().lower() == "yes"
        except ImportError:
            show_monthly = input("Do you want to see monthly salary breakdowns? (y/n): ").strip().lower() in ["y", "yes"]

        hourly_wage = calculate_hourly_wage(monthly_pay, working_days_per_week, hours_per_day)

        gross_salary = 0.0
        total_deductions = 0.0
        current = join_date.replace(day=1)

        print("\nEnter leave details for each month (from joining to current):")
        while current <= today.replace(day=1):
            year, month = current.year, current.month
            month_label = current.strftime("%B %Y")
            total_working_days = count_working_days(year, month, working_days_per_week)

            # Prorate first month
            if year == join_date.year and month == join_date.month:
                start_day = join_date.day
                month_days = [datetime(year, month, day)
                              for day in range(start_day, calendar.monthrange(year, month)[1] + 1)]
                working_days = sum(1 for d in month_days if d.weekday() < (6 if working_days_per_week == 6 else 5))
            else:
                working_days = total_working_days

            print(f"\n{month_label}:")
            full_leaves = get_valid_int_input("  Number of full leave days: ", 0, 31)
            half_days = get_valid_int_input("  Number of half-days: ", 0, 31)

            # Salary and deductions
            month_salary = (working_days / total_working_days) * monthly_pay if total_working_days else 0
            gross_salary += month_salary

            # --- CHANGED LOGIC BELOW ---
            effective_working_days = working_days  # For both joining and regular months
            # Prevent division by zero
            if effective_working_days == 0:
                daily_wage = 0
            else:
                daily_wage = month_salary / effective_working_days

            total_leave_days = min(full_leaves + 0.5 * half_days, effective_working_days)
            month_deduction = total_leave_days * daily_wage
            total_deductions += month_deduction

            month_net_salary = month_salary - month_deduction

            # Conditional Monthly Output
            if show_monthly:
                print(f"  → Prorated Gross: ₹{month_salary:.2f}")
                print(f"  → Deductions: ₹{month_deduction:.2f}")
                print(f"  → Net Salary for {month_label}: ₹{month_net_salary:.2f}")

            # Go to next month
            current = (current.replace(day=28) + timedelta(days=4)).replace(day=1)

        net_salary = gross_salary - total_deductions

        print("\n--- Final Salary Summary ---")
        print(f"Reference hourly wage: ₹{hourly_wage:.2f}")
        print(f"Gross salary (prorated): ₹{gross_salary:.2f}")
        print(f"Total deductions: ₹{total_deductions:.2f}")
        print(f"Net salary: ₹{net_salary:.2f}")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
