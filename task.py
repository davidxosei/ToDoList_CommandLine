import json

FILE_NAME = "data.json"

def load_data():
    with open(FILE_NAME, 'r') as task_data:
        return json.load(task_data)
    
def display_data():
    data = load_data()
    if not data["tasks"] and not data["category"]:
        print("No tasks or categories available")
        return
    hmap = {}

    for category in data["category"]:
        hmap[category["id"]] = {"name": category["name"], "tasks": []}

    for task in data["tasks"]:
        cat_id = task["category_id"]
        if cat_id in hmap:
            hmap[cat_id]["tasks"].append(task["name"])

    for cat in hmap.values():
        print(f"\nCategory: {cat['name']}")
        if not cat["tasks"]:
            print("  (No tasks)")
        else:
            for task_name in cat["tasks"]:
                print(" -", task_name)

    
def add_task():
    task_name = input("Enter task name: ")
    valid_response = False

    while(not valid_response):
        response = input("Would you like to assign "+ task_name + " to a category? Y/N ").upper()
        if(response == "Y" or response == "YES"):
            category = input("Enter category: ").lower().strip()
            category_id = add_category(category)
        else:
            category_id = add_category("none")
        valid_response = True
    data = load_data()
    new_task_id = max([task["id"] for task in data["tasks"]] + [0]) + 1
    data["tasks"].append({"id": new_task_id, "name": task_name, "category_id": category_id})
    save_data(data)

def add_category(requested_category_name):
    data = load_data()
    for category in data["category"]:
        if category["name"] == requested_category_name:
            return category["id"]
    new_category_id = max([category["id"] for category in data["category"]] + [0]) + 1
    data["category"].append({"id": new_category_id, "name": requested_category_name})
    save_data(data)
    return new_category_id


def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=2)


def remove_task():
    data = load_data()
    for task in data["tasks"]:
        print(f'{task["name"]}: (id - {task["id"]})')

    while True:
        try:
            id = int(input("Enter the id of the task you'd like to delete or enter 0 to cancel."))
            if id == 0:
                break
            task_found = False
            new_data = []
            for task in data["tasks"]:
                if task["id"] == id:
                    deleted_task_name = task["name"]
                    task_found = True
                    print("Deleting task: ", deleted_task_name)
                else:
                    new_data.append(task)
                    
            if(not task_found):
                raise ValueError
            data["tasks"] = new_data
            save_data(data)
            break
        except ValueError:
            print("Invalid id.")
            continue
    
if __name__ == "__main__":
    while(True):
        print()
        print("To-do List Main menu")
        print("Select an option: 1-4")
        print("1. Load tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")
        print()
        try:
            option = int(input("Option: "))
            print()
            if option > 4 or option < 1:
                raise ValueError
        except ValueError:
            print("Please select a valid option")
            print()
        
        if option == 1:
            print("Displaying tasks")
            print()
            display_data()
        elif option == 2:
            add_task()
        elif option == 3:
            remove_task()
        elif option == 4:
            print("Quitting app..")
            break