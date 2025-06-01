

def main():
    
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    print()  

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. You should work on it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Consider completing it this week.")
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task but has a deadline today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level entered. Please use high, medium, or low.")


    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("\n🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()
