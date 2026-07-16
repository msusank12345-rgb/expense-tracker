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
        print("3. Search by Category")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
         add_expense()
        elif choice == "2":
         view_expenses()
        elif choice == "3":
         search_by_category()
        elif choice == "4":
         delete_expense()
        elif choice == "5":
         print("Thank you for using Expense Tracker. Goodbye!")
         break
        else:
         print("Invalid choice!")


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, f"{amount:.2f}"])

    print("\nExpense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n===== Your Expenses =====")
        print("=" * 60)

        total = 0
        count = 0

        # Skip the header row
        next(reader, None)

        for row in reader:
            print(" | ".join(row))
            count += 1

            # Amount is in the last column
            total += float(row[3])

        print("-" * 60)
        print(f"Total records: {count}")
        print(f"Total spent: Rs. {total:.2f}")

def search_by_category():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    category = input("\nEnter category to search: ").strip().lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader, None)

        found = False

        print("\nMatching Expenses")
        print("-" * 50)

        for row in reader:
            if row[1].lower() == category:
                print(" | ".join(row))
                found = True

        if not found:
            print("No matching expenses found.")
def delete_expense():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("\nNo expenses to delete.")
        return

    print("\n===== Expenses =====")

    for i, row in enumerate(reader[1:], start=1):
        print(f"{i}. {' | '.join(row)}")

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(reader) - 1:
            deleted = reader.pop(choice)

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)

            print(f"\nDeleted: {' | '.join(deleted)}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()