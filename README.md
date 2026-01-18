# Task Tracker CLI


A simple command-line based task-tracker application written in Python. This program allows its users to manage their tasks by adding, listing, editing and deleting the tasks. The program uses a JSON file for data persistence.


## Features:
- Adding tasks
- Editing existing tasks
- Listing tasks
- Removing tasks
- Data persistence with JSON
- Input validation for crash management
- Simple user-friendly menu



## Technologies Used:
- Python
- JSON
- CLI

## Concepts and Skills:
- Functions and modular programming
- Lists and dictionaries
- Input validation
- JSON serialization & deserialization
- Loops
- Command-line interface design
- Basic error handling

## How to Run:
1. Make sure to have Python 3 installed.
2. Clone the repository
	
		git clone https://github.com/OmerHarmankayaC/Task_Tracker.git
3. Run the program

   		python main.py

## Data Storage

Each task is stored as a dictionary with the following format in the tasks.json file

	{
  	"title": "Finish assignment",
  	"desc": "Complete Python task tracker project",
  	"dueDate": "2026-01-20"
	}

## Error Handling

The common types of input errors in this program are ValueErrors

To prevent errors to distrupt the user, this program uses simple error handling mechanisms right before the input is going to be used.

The program checks if the input value is in the desired type, if not asks user to re-enter the value.

Other types of errors include:
- FileNotFoundError: Creates a new file if there isn't one
- JSONDecodeError: Creates a new file if the current one is corrupted
 
## Possible Improvements

- Adding completed attribute to tasks. So that the users can mark the tasks when they complete them.
- The completed attribute can be used for further improvement such as, creating an interface where the user can only see the tasks that they completed or vice versa.
- Due-date validation
- Prioritizing tasks

## About the Author

Ömer Harmankaya

Computer Engineering student at TED University

This project was developed as part of personal learning and skill improvement.
