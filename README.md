# To-Do List Command-Line App

## Approach and Design

This is a simple command-line to-do list app built with Python. It uses a JSON file (data.json) to persist data across sessions. Each task can be optionally assigned to a category. Categories are stored separately and linked to tasks using a category_id field. 
The app uses IDs to uniquely identify both tasks and categories.

The user interacts with the program through a simple numbered menu. Functions are separated logically by purpose: loading/saving data, adding tasks, removing tasks, displaying tasks, and managing categories.

## Key Files and Folders


- task.py contains all program functions and the main menu loop.
- data.json is the file where tasks and categories are saved.
- No additional folders or dependencies are required.

## Process to Run, Test, and Verify

### Requirements
- Python 3.x installed

### To run the application:
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the application using: python task.py

4. Use the on-screen menu to:
- View tasks grouped by category
- Add a new task with or without a category
- Remove an existing task by its ID
- Quit the application

### To verify:
- Tasks and categories will persist between runs in data.json.
- Running the app again will show updated task data.

## Test Data

You can copy and paste this into data.json before running the app:

{
"tasks": [
 { "id": 1, "name": "Do Laundry", "category_id": 1 },
 { "id": 2, "name": "Finish project", "category_id": 2 }
],
"category": [
 { "id": 1, "name": "cleaning" },
 { "id": 2, "name": "work" }
]
}
This seed data will result in two tasks under two separate categories.
