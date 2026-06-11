import csv
import os
from datetime import datetime

# CSV file name
FILE_NAME = "expense_data.csv"

# Column headers for the CSV file
COLUMNS = ["Expense_ID", "Date", "Description", "Amount", "Category"]


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)


# Add a new expense record
def record_expense():

    # Get expense details from user
    description = input("Enter expense description: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    # Validate amount
    try:
        amount = float(amount)
    except ValueError:
        print("Please enter a valid amount.")
        return

    # Generate unique expense ID
    expense_id = "EXP" + str(int(datetime.now().timestamp()))

    # Save expense to CSV file
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense_id,
            datetime.now().strftime("%Y-%m-%d"),
            description,
            amount,
            category.title()
        ])

    print("Expense saved successfully!")


# Display all stored expenses
def display_expenses():

    create_file()

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        records = list(csv.reader(file))

    # Check if file contains any expense records
    if len(records) <= 1:
        print("No expense records available.")
        return

    print("\n========== Expense Records ==========")

    total_amount = 0

    # Display each expense record
    for row in records[1:]:

        print(
            f"ID: {row[0]} | Date: {row[1]} | "
            f"Description: {row[2]} | Amount: ₹{row[3]} | Category: {row[4]}"
        )

        total_amount += float(row[3])

    # Display overall spending
    print(f"\nOverall Spending: ₹{total_amount:.2f}")


# Search expenses by category
def find_by_category():

    create_file()

    search_category = input("Enter category to search: ")

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        records = list(csv.reader(file))[1:]

    matched_records = []

    # Find matching records
    for row in records:
        if row[4].lower() == search_category.lower():
            matched_records.append(row)

    if not matched_records:
        print("No expenses found in this category.")
        return

    print("\nMatching Expenses:")

    # Display matching records
    for row in matched_records:
        print(
            f"Date: {row[1]} | "
            f"Description: {row[2]} | "
            f"Amount: ₹{row[3]}"
        )


# Generate monthly expense report
def calculate_monthly_total():

    create_file()

    month = input("Enter month (YYYY-MM): ")

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        records = list(csv.reader(file))[1:]

    monthly_expense = 0

    # Calculate total expenses for selected month
    for row in records:
        if row[1].startswith(month):
            monthly_expense += float(row[3])

    print(f"Total expenditure for {month}: ₹{monthly_expense:.2f}")


# Main menu function
def main_menu():

    create_file()

    while True:

        print("\n====== Expense Management System ======")
        print("1. Record Expense")
        print("2. Display Expenses")
        print("3. Find by Category")
        print("4. Monthly Report")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            record_expense()

        elif option == "2":
            display_expenses()

        elif option == "3":
            find_by_category()

        elif option == "4":
            calculate_monthly_total()

        elif option == "5":
            print("Thank you for using Expense Management System!")
            break

        else:
            print("Invalid option. Please try again.")


# Program starts here
if __name__ == "__main__":
    main_menu()
