tasks = []

def add_task():
    title = input("Please enter your task title: ")
    exp = input("Please enter the explanation: ")
    dueDate = input("Please enter the due-date: ")

    tasks.append({"title": title,
              "exp": exp,
              "dueDate": dueDate})

def delete_task():
    if (len(tasks) == 0):
        print("You don't have any tasks!")
        return
    
    while True:
        print("Enter \"exit\" to return to main menu.")
        deleteIndex = input("Please enter the task number that you want to delete: ")
        
        if (deleteIndex.casefold() == "exit"):
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
    
    for index, i in enumerate(tasks, start = 1):
        print(index, "-", i["title"], ":", i["exp"], ";", i["dueDate"])

while True:
    print("1-See my tasks")
    print("2-Add a new task")
    print("3-Delete a task")
    print("4-Exit")

    opr = input("Please enter your operation: ")

    if (opr == "1"):
        list_tasks()
    
    elif (opr == "2"):
        add_task()

    elif (opr == "3"):
        list_tasks()
        delete_task()

    elif (opr == "4"):
        print("Terminating the program...")
        break