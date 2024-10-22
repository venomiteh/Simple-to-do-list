def display_menu():
    print("What would you like to do?\n")
    print("1-Add a task")
    print("2-view tasks")
    print("3-Delete tasks")
    print("4-Exit")
    

def add_task(tasks):
    task:str = input("Enter the task you would like to add")
    tasks.append(task)

def display_task(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("You Don't Have any tasks!")
        return
    for k, task in enumerate(tasks, start=1):
        print(f'"{k}"- "{task}"')

                 
def remove_task(tasks):
    display_task(tasks)
    if not tasks:
        return
    while True:
        try:
            choice = int(input("Enter the task number you would like to remove: "))
            if 1 <= choice <= len(tasks):  
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    rm_task = tasks.pop(choice - 1)  
    print(f'Task "{rm_task}" has been removed.')

def main():
    tasks=[]
    while True:
        display_menu()
        choice = input("Please enter your choice:")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice please try again!")



main()




















