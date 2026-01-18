import json

tasks = []

def add_task():
    title = input("Please enter your task title: ")
    desc = input("Please enter the description: ")
    dueDate = input("Please enter the due-date: ")

    tasks.append({"title": title,
              "desc": desc,
              "dueDate": dueDate})

def delete_task():
    if (len(tasks) == 0):
        print("You don't have any tasks!")
        return
    
    while True:
        print("Enter \"exit\" to return to main menu.")
        deleteIndex = input("Please enter the task number that you want to delete: ")
        
        if (deleteIndex.casefold() == "exit"):
            print("Returning to the main menu...")
            return
        
        elif (int(deleteIndex) < 1 or int(deleteIndex) > len(tasks)):
            print("Please enter a viable number!")
        
        else:
            tasks.pop(int(deleteIndex) - 1)
            print("Task has been succesfully removed!")
            return

def list_tasks():
    if (len(tasks) == 0):
        print("You don't have any tasks!")
        return
    
    for index, i in enumerate(tasks, start = 1):
        print(index, "-", i["title"], ":", i["desc"], ";", i["dueDate"])

def edit_task():
    if (len(tasks) == 0):
        print("You don't have any tasks!")
        return

    while True:
        list_tasks()
        print("Enter \"exit\" to return to the menu.")
        editIndex = input("Please enter the task number that you want to edit: ")

        if (editIndex.casefold() == "exit"):
            print("Returning to the main menu...")
            return
        
        elif (int(editIndex) < 1 or int(editIndex) > len(tasks)):
            print("Please enter a viable number!")

        else:
            while True:
                print("1-Title")
                print("2-Description")
                print("3-Due-date")
                print("4-Edit a different task")
                print("5-Return to main menu")

                editType = int(input("Enter the number that you want to edit: "))
                task = tasks[int(editIndex) - 1]

                if (editType == 4):
                    break
                
                elif (editType == 5):
                    print("Returning to the main menu.")
                    return

                elif (editType == 1):
                    newTitle = input("Enter the new title: ")
                    task["title"] = newTitle

                elif (editType == 2):
                    newDesc = input("Enter the new description: ")
                    task["desc"] = newDesc

                elif (editType == 3):
                    newDate = input("Enter the new due-date: ")
                    task["dueDate"] = newDate

def load_json():
    try:
        with open("Tasks.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError):
        with open("tasks.json", "w") as file:
            json.dump([], file, indent = 4)
        return []
    
    except (json.JSONDecodeError):
        print("tasks.jason is corrupted, reseting the file...")
        with open("tasks.json", "w") as file:
            json.dump([], file, indent = 4)
        return []

def write_json():
    with open("Tasks.json", "w") as file:
        json.dump(tasks, file, indent = 4)

tasks = load_json()

while True:
    print("1-See my tasks")
    print("2-Add a new task")
    print("3-Delete a task")
    print("4-Edit a task")
    print("5-Exit")

    opr = input("Please enter your operation: ")

    if (opr == "1"):
        list_tasks()
    
    elif (opr == "2"):
        add_task()
        write_json()

    elif (opr == "3"):
        list_tasks()
        delete_task()
        write_json()

    elif (opr == "4"):
        edit_task()
        write_json()

    elif (opr == "5"):
        print("Terminating the program...")
        break