import csv
import os

FILE_NAME = "expenses.csv"


def main():
    print("Welcome to Expense Tracker!")
    while True:
        print("\n" + "=" * 40)
        print("Expense Tracker")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice!")


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("\nExpense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\nYour Expenses:")
        print("-" * 50)

        count = 0

        for row in reader:
          print(" | ".join(row))
          count += 1

        print("-" * 50)
        print(f"Total records: {count - 1}")

if __name__ == "__main__":
    main()