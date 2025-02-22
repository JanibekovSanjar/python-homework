import csv
import json

columns = ['id', 'title', 'description', 'date', 'status']


class App:
    def __init__(self, file_base_name, file_type):
        self.type = file_type
        self.file_base_name = file_base_name
        self.source_path = f"{self.file_base_name}.{self.type}"
        self.data = []

    def read_csv(self):
        try:
            with open(self.source_path, newline='') as f:
                cont = csv.DictReader(f)
                self.data = list(cont)
        except FileNotFoundError:
            print("CSV file not found. Starting fresh.")

    def read_json(self):
        try:
            with open(self.source_path) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("JSON file not found. Starting fresh.")

    def display(self):
        if not self.data:
            print("No tasks available.")
        else:
            for task in self.data:
                print(task)

    def update(self, task_id, key, val):
        for row in self.data:
            if row['id'] == task_id:
                row[key] = val
                print("Updated successfully.")
                return
        print("Task ID not found.")

    def delete(self, task_id):
        for i, row in enumerate(self.data):
            if row['id'] == task_id:
                del self.data[i]
                print("Deleted successfully.")
                return
        print("Task ID not found.")

    def display_filter(self, status):
        filtered = [row for row in self.data if row['status'].lower() == status.lower()]
        if filtered:
            for task in filtered:
                print(task)
        else:
            print(f"No tasks with status '{status}' found.")

    def add_task(self, task):
        self.data.append(task)
        print("Task added successfully.")

    def save(self):
        if self.type == 'csv':
            with open(self.source_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader()
                writer.writerows(self.data)
        elif self.type == 'json':
            with open(self.source_path, 'w') as f:
                json.dump(self.data, f, indent=4)
        print("Tasks saved successfully.")

    def load(self):
        if self.type == 'csv':
            self.read_csv()
        elif self.type == 'json':
            self.read_json()
        print("Tasks loaded successfully.")


class Manager:
    def __init__(self):
        file_type = input("Choose file format (csv/json): ").strip().lower()
        if file_type not in ["csv", "json"]:
            print("Invalid choice. Defaulting to CSV.")
            file_type = "csv"

        self.app = App('f', file_type)

        self.command_dict = {
            '1': self.add_task,
            '2': self.app.display,
            '3': self.update_task,
            '4': self.delete_task,
            '5': self.filter_tasks,
            '6': self.app.save,
            '7': self.app.load
        }

    def menu(self):
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

    def add_task(self):
        task = {
            "id": input("Enter Task ID: ").strip(),
            "title": input("Enter Title: ").strip(),
            "description": input("Enter Description: ").strip(),
            "date": input("Enter Due Date (YYYY-MM-DD): ").strip(),
            "status": input("Enter Status (Pending/In Progress/Completed): ").strip().capitalize()
        }
        self.app.add_task(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        key = input("Enter the field to update (title/description/date/status): ").strip().lower()
        val = input("Enter new value: ").strip()
        self.app.update(task_id, key, val)

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        self.app.delete(task_id)

    def filter_tasks(self):
        status = input("Enter status to filter (Pending/In Progress/Completed): ").strip().capitalize()
        self.app.display_filter(status)

    def start(self):
        self.app.load()  # Load existing tasks on startup

        while True:
            self.menu()
            command = input("Enter your choice: ").strip()

            if command == '8':
                print("Exiting To-Do Application.")
                break

            action = self.command_dict.get(command)
            if action:
                action()
            else:
                print("Invalid option. Please choose a valid number.")


# Run the application
if __name__ == "__main__":
    m = Manager()
    m.start()
