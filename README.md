# 💰 Pro-Rated Salary Calculator CLI (Python)

> A modern, interactive command-line tool to calculate employee salary based on joining date, workdays per week, hours per day, and leave deductions — **ideal for freelancers, HR professionals, finance teams, and employees**.

---

## 🚀 Features

- 🔢 Calculates **prorated salary** for partial joining months
- 📆 Supports **custom workweeks** (5 or 6 days/week)
- ⏰ Calculates **hourly wage** based on working hours/day
- 📉 Deducts salary for **full** and **half-day leaves**
- 📊 Provides a **monthly breakdown** and **final summary**
- 💬 Interactive UI using arrows and selections via `questionary`
- 🎨 Cool CLI header banner using `pyfiglet`

---

## 🎯 Use Cases

- HR teams calculating **new joiner or exit month salaries**
- Freelancers tracking **billable vs non-billable days**
- Employees checking **net take-home after leaves**
- Startups or small businesses without complex HR software

---
## 🧮 Salary Calculator – Logic Overview
This script calculates your net salary for each month, considering your joining date, leaves taken, and working schedule. Here’s how it works:

#### 1. User Inputs
> Monthly Pay: Your gross monthly salary.

> Working Days per Week: How many days you work each week (typically 5 or 6).

> Hours Worked per Day: Your daily working hours.

> Joining Date: The date you started your job.

> Leave Details: For each month (from joining to current), you enter the number of full and half-day leaves.

#### 2. Working Days Calculation
> The script calculates the total number of working days in each month, based on your working days per week (Mon–Fri or Mon–Sat).

> For your joining month, it only counts working days from your joining date to the end of that month.

#### 3. Salary Proration
> For the joining month, your gross salary is prorated based on the number of eligible working days.

> For subsequent months, the full monthly salary is considered.

#### 4. Leave Deductions
> For each month, you enter how many full and half-day leaves you took.

> The script calculates your per-day wage (using 22 days for a 6-day week or 20 for a 5-day week).

> Deduction = (Full Leaves + 0.5 × Half-Days) × Per-Day Wage

> Deductions are capped so you can't be deducted for more days than you could have worked.

#### 5. Net Salary Calculation
> Net Salary = Prorated Gross Salary – Deductions

> The script shows a breakdown for each month (if you choose), and a final summary including:

> Reference hourly wage

> Total gross salary (prorated)

> Total deductions

> Net salary

#### 6. Monthly Breakdown (Optional)
> You can opt to see detailed monthly breakdowns, which include gross, deductions, and net pay for each month.

> Example Calculation
> Suppose you:

> Join on March 17, 2025

> Work 6 days/week, 8 hours/day

> Monthly pay is ₹39,618

> Take 1 full leave and 1 half-day in March

> The script will:

> Count working days from March 17–31

Prorate your salary for those days

> Deduct your leave days at the calculated per-day rate

> Display your net salary for March and each following month

> Key Points
> Flexible: Works for any joining date, working schedule, and leave pattern.

> Accurate: Prorates salary for partial months and deducts leaves precisely.

> Interactive: Guides you step-by-step for easy data entry.


---
## 🖥️ Demo

```shell
 ____    _    _        _    ______   __
/ ___|  / \  | |      / \  |  _ \ \ / /
\___ \ / _ \ | |     / _ \ | |_) \ V / 
 ___) / ___ \| |___ / ___ \|  _ < | |  
|____/_/   \_\_____/_/   \_\_| \_\|_|  
                                       
  ____    _    _     ____ _   _ _        _  _____ ___  ____  
 / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
| |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
| |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
 \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\
                                                             

Enter your monthly pay (in ₹): 29617
Enter the number of working days per week (e.g., 5 or 6): 6
Enter hours worked per day (1–24): 8

Monthly Pay: ₹29617.0
Working Days/Week: 6
Hours Per Day: 8
Enter your joining date (DD-MM-YYYY): 25-02-2025
? Do you want to see monthly salary breakdowns? Yes

Enter leave details for each month (from joining to current):

February 2025:
  Number of full leave days: 0
  Number of half-days: 0
  → Prorated Gross: ₹4936.17
  → Deductions: ₹0.00
  → Net Salary for February 2025: ₹4936.17

March 2025:
  Number of full leave days: 0
  Number of half-days: 0
  → Prorated Gross: ₹29617.00
  → Deductions: ₹0.00
  → Net Salary for March 2025: ₹29617.00

April 2025:
  Number of full leave days: 1
  Number of half-days: 1
  → Prorated Gross: ₹29617.00
  → Deductions: ₹2019.34
  → Net Salary for April 2025: ₹27597.66

May 2025:
  Number of full leave days: 2
  Number of half-days: 2
  → Prorated Gross: ₹29617.00
  → Deductions: ₹4038.68
  → Net Salary for May 2025: ₹25578.32
```

---

## 🛠️ Installation

⚠️ Python 3.8+ required

```shell
git clone https://github.com/DinoQuinten/salary-calculator-tool.git
cd salary-calculator-tool
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ❓ FAQ

**Q: Can I calculate salaries for past months?**  
A: Yes! It supports joining date-based looping from the past up to today.

**Q: Will this handle 4-day work weeks?**  
A: Currently supports 5 or 6 days/week. You can extend `get_valid_int_input()` to accept 4.

**Q: Can I export the output?**  
A: Not yet, but you can redirect output using:  
   `python smart-salary-calculator.py > salary_summary.txt`

---

## ▶️ How to run

By default, the main script is named `smart-salary-calculator.py`.  
If you prefer the name `salary_calculator_cli.py`, you can rename it:

```shell
mv smart-salary-calculator.py salary_calculator_cli.py
python salary_calculator_cli.py
```

Or simply run:

```shell
python smart-salary-calculator.py
```

---

## 🌍 SEO Keywords (for discoverability)

salary calculator Python, prorated salary script, calculate salary with leaves, half day salary deduction, joining date salary calculator, HR tool Python, freelance salary tracker, Python CLI payroll, part-time pay calculator, command-line salary calculator

---

## 🤝 Contributing

Pull requests welcome! Please open an issue to discuss major changes.

---

## 🙌 Author

Prasanna  
GitHub: [@DinoQuinten](https://github.com/DinoQuinten/)
