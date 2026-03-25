# Your name here...

def read_file(filename):
    # THis should be replaced with proper code
    return [],[],[],[]

def menu():
    filename = "college.txt"
    ids, gdpr, days, status = read_file(filename)
    choice = ""
    while choice != "8":
        print("\nMenu")
        print("1. View all players")
        print("2. Delete a player")
        print("3. Register new player")
        print("4. Update player status")
        print("5. Placeholder for Exam")
        print("6. Placeholder for Exam")
        print("7. Placeholder for Exam")
        print("8. Quit and save")
        choice = input("Enter choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == '7':
            pass
        elif choice == "8":
            pass
            print("Data saved. Goodbye.")
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    menu()