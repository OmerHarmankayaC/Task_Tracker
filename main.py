tasks = []

def add_task():
    title = input("Please enter your task title: ")
    exp = input("Please enter the explanation: ")
    dueDate = input("Please enter the due-date: ")

    tasks.append({"title": title,
              "exp": exp,
              "dueDate": dueDate})

def list_tasks():
    if (len(tasks) == 0):
        print("You don't have any tasks!")
    
    for index, i in enumerate(tasks, start = 1):
        print(index, "-", i["title"], ":", i["exp"], ";", i["dueDate"])

while True:
    print("1-See my tasks")
    print("2-Add a new task")
    print("3-Exit")

    opr = input("Please enter your operation: ")

    if (opr == "1"):
        list_tasks()
    
    if (opr == "2"):
        add_task()

    if (opr == "3"):
        print("Terminating the program...")
        break