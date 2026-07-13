import csv
import os

FILE_NAME = "expenses.csv"


def main():
    while True:
        print("\n" + "=" * 40)
        print("      Expense Tracker")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


def add_expense():
    pass


def view_expenses():
    pass


if __name__ == "__main__":
    main()