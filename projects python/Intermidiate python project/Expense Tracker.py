import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# Database setup
def setup_database():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add expense
def add_expense(date, category, amount, description=""):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    print("\nAll Expenses:")
    for row in rows:
        print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]:.2f}, Description: {row[4]}")

# Monthly summary
def monthly_summary(month, year):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, SUM(amount) 
        FROM expenses 
        WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY category
    ''', (f"{month:02}", str(year)))
    rows = cursor.fetchall()
    conn.close()

    print(f"\nMonthly Summary for {month}/{year}:")
    total = 0
    summary = {}
    for row in rows:
        print(f"Category: {row[0]}, Total: ${row[1]:.2f}")
        summary[row[0]] = row[1]
        total += row[1]
    print(f"Overall Total: ${total:.2f}")
    return summary

# Visualization
def visualize_summary(summary):
    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Distribution")
    plt.show()

# Main menu
def main():
    setup_database()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. Visualize Monthly Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter a description (optional): ")
            add_expense(date, category, amount, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year (e.g., 2025): "))
            summary = monthly_summary(month, year)
        elif choice == "4":
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year (e.g., 2025): "))
            summary = monthly_summary(month, year)
            if summary:
                visualize_summary(summary)
            else:
                print("No expenses to visualize.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
