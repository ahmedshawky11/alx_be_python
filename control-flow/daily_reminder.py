task=input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time=input("Is it time-bound? (yes/no): ").lower()
if time=="yes":
    if priority=="high":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    elif priority=="medium":
        print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
    else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    if priority=="high":
        print(f"Reminder: '{task}' is a high priority task that requires attention today!")
    elif priority=="medium":
        print(f"Reminder: '{task}' is a medium priority task that requires attention!")
    else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
