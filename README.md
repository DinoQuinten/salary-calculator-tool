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

--- Final Salary Summary ---
Reference hourly wage: ₹168.28
Gross salary (prorated): ₹93787.17
Total deductions: ₹6058.02
Net salary: ₹87729.14
```