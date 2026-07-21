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
        print("4. Search by Date")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Sort Expenses by Amount")
        print("8. Monthly Report")
        print("9. Expense Summary")
        print("10. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
         add_expense()
        elif choice == "2":
         view_expenses()
        elif choice == "3":
         search_by_category()
        elif choice == "4":
         search_by_date()
        elif choice == "5":
         delete_expense()
        elif choice == "6":
          edit_expense()
        elif choice == "7":
         sort_by_amount()
        elif choice == "8":
         monthly_report()
        elif choice == "9":
         expense_summary()
        elif choice == "10":
         print("Thank you for using Expense Tracker. Goodbye!")
         break
        else:
         print("Invalid choice.")

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    while True:
        try:
           amount = float(input("Enter amount: "))
           if amount <= 0:
             print("Amount must be greater than 0.")
             continue

           break

        except ValueError:
          print("Please enter a valid number.")
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
        print("Date | Category | Description | Amount")
        print("-" * 50)

        for row in reader:
            if row[1].lower() == category:
                print(" | ".join(row))
                found = True

        if not found:
            print("No matching expenses found.")

def search_by_date():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    date = input("\nEnter date (YYYY-MM-DD): ").strip()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader, None)

        found = False

        print("\nMatching Expenses")
        print("Date | Category | Description | Amount")
        print("-" * 50)

        for row in reader:
            if row[0] == date:
                print(" | ".join(row))
                found = True

        if not found:
            print("No expenses found for that date.")

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
        
def edit_expense():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("\nNo expenses to edit.")
        return

    print("\n===== Expenses =====")
    for i, row in enumerate(rows[1:], start=1):
        print(f"{i}. {' | '.join(row)}")

    try:
        choice = int(input("\nEnter expense number to edit: "))

        if 1 <= choice <= len(rows) - 1:
            print("\nLeave blank to keep the current value.")

            current = rows[choice]

            date = input(f"Date ({current[0]}): ") or current[0]
            category = input(f"Category ({current[1]}): ") or current[1]
            description = input(f"Description ({current[2]}): ") or current[2]
            
            while True:
               amount = input(f"Amount ({current[3]}): ")

               if amount == "":
                amount = current[3]
                break

                try:
                    if float(amount) <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid amount.")

            rows[choice] = [date, category, description, amount]

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Updated Expense:")
            print(" | ".join(rows[choice]))

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
def sort_by_amount():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        expenses = list(reader)

    if not expenses:
        print("\nNo expenses to sort.")
        return

    expenses.sort(key=lambda row: float(row[3]), reverse=True)

    print("\n===== Expenses Sorted by Amount (Highest to Lowest) =====")
    print("=" * 60)

    for row in expenses:
        print(" | ".join(row))
    total = sum(float(row[3]) for row in expenses)

    print("-" * 60)
    print(f"Total Expenses: Rs. {total:.2f}")

def monthly_report():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    month = input("\nEnter month (YYYY-MM): ").strip()

    total = 0
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        print(f"\n===== Expenses for {month} =====")
        print("-" * 60)

        for row in reader:
            if row[0].startswith(month):
                print(" | ".join(row))
                total += float(row[3])
                found = True

    if found:
        print("-" * 60)
        print(f"Total spent in {month}: Rs. {total:.2f}")
    else:
        print("No expenses found for this month.")

def expense_summary():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[3])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("\nNo expenses found.")
        return

    print("\n===== Expense Summary =====")
    print("-" * 40)

    grand_total = 0

    for category, amount in summary.items():
        print(f"{category:<15} Rs. {amount:.2f}")
        grand_total += amount

    print("-" * 40)
    print(f"Grand Total: Rs. {grand_total:.2f}")

if __name__ == "__main__":
    main()