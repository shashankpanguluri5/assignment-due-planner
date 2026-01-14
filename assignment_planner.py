def show_menu():
    print("\n=== Assignment Due Planner ===")
    print("1. Add assignment")
    print("2. View assignments")
    print("3. Mark assignment as completed")
    print("4. Exit")

assignments = []

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Assignment name: ")
        course = input("Course: ")
        due_date = input("Due date (YYYY-MM-DD): ")
        priority = input("Priority (High/Medium/Low): ")

        assignment = {
            "name": name,
            "course": course,
            "due": due_date,
            "priority": priority,
            "completed": False
        }

        assignments.append(assignment)
        print("Assignment added!")

    elif choice == "2":
        if not assignments:
            print("No assignments yet.")
        else:
            for i, a in enumerate(assignments, start=1):
                status = "Done" if a["completed"] else "Pending"
                print(f"{i}. {a['name']} | {a['course']} | Due: {a['due']} | {a['priority']} | {status}")

    elif choice == "3":
        num = int(input("Enter assignment number: ")) - 1
        if 0 <= num < len(assignments):
            assignments[num]["completed"] = True
            print("Marked as completed.")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
