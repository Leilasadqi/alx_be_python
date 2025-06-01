task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base = f"Reminder: '{task}' is a low priority task"
    case _:
        base = f"Reminder: '{task}' has an unspecified priority"

print(f"{base}" + ( " that requires immediate attention today!" if time_bound == "yes" and priority in ["high", "medium"] else " that should be done soon." if time_bound == "yes" else ". Consider completing it when you have free time." if priority == "low" else "." ))
