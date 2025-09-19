# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task with match-case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Adjust message if time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        message = "Note: " + message + ". Consider completing it when you have free time."

# Output the reminder
print(f"Reminder:", message)