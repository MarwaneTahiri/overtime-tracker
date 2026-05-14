# OVERTIME TRACKER

This is a simple overtime tracker app that helps you keep track of the hours you’ve worked by letting you log them.

---

# FEATURES

## Command Line Interface

The app uses a CLI to keep things simple and easy to use. You get 4 options:

1. Log overtime  
2. View total hours  
3. Target pay calculator  
4. Exit  

---

## Feature 1: Log new overtime

When logging overtime, the app asks for a date in DD-MM-YY format and the number of hours worked. 

---

## Feature 2: View total hours

You can view the total number of hours logged. 

---

## Feature 3: Target pay calculator

This feature asks for your hourly wage and how much you want to earn this month. It then calculates how many hours you need to work to reach that target.

---

# HOW TO USE

1. Run the `Overtime_Tracker.py` file  
2. Use the CLI to access the features  

# FUTURE IMPROVEMENTS

- Add an option to view all logged overtime entries by date
- Add input validation so the app handles invalid dates, blank inputs, and non-number values
- Allow users to edit or delete existing overtime entries
- Improve the JSON data structure to store each entry with clear `date` and `hours` fields
- Add monthly totals so users can see overtime for a specific month
- Update the target pay calculator to use monthly overtime instead of all time overtime
- Add a CSV export so overtime records can be opened in a spreadsheet
- Add basic tests for the main calculations
- Build a simple GUI or web version 