class Task:
    """ Class 'Task' created and instantiated with method taking attributes task ID, 
    task description and completion date"""
    def __init__(self, task_id, task_description, completion_date):
        self.task_id = task_id
        self.task_description = task_description
        self.completion_date = completion_date

    def add_task(task_description, completion_date):
        """ C(reate): adding a new task"""
        # The ID values are consecutive, so the new task would have the next number not 
        # already included in the task list.
        new_id = len(tasks_list) +1
        # New task list assigned new ID, and description and completion date taken as attributes.
        new_task = Task(new_id, task_description, completion_date)
        # New task is added to the existing task list.
        tasks_list.append(new_task)
        # Prints message to the user to notify them the new task they have added has been done so successfully.
        print(f"You have added a new task due {completion_date} successfully.")
         
    def read_task(task_id):
        """ R(ead): reading task from task list."""
        # Iterates through each list item.
        for task in tasks_list:
            # If task ID given matches a task ID in the list, statemement is executed.
            if task.task_id == task_id:
                print(f"'{task.task_description}' Complete this task by {task.completion_date}.")
            # If the task ID given does not match a task ID in the list, the user is notified.
            else:
                print(f"Task ID {task_id} not found.")

    def amend_task(task_id, new_description, new_completion_date):
        """ U(pdate): task is chosen by ID and amended."""
        # Iterates through each list item.
        for task in tasks_list:
            # If task ID given matches a task ID in the list, the task description and 
            # completion date for the chosen task can be amended.
            if task.task_id == task_id:
                task.task_description = new_description
                task.completion_date = new_completion_date
                # Prints message back to the user to notify them the changes have been made successfully.
                print(f"You have successfully amended your task. '{new_description}' is due to be completed by {new_completion_date}") 
            else:
                # If the task ID given does not match a task ID in the list, the user is notified.
                print(f"Task ID {task_id} not found.")

    def delete_task(task_id):
        """ D(elete): delete task from task list by given task ID."""
        # Each list item including all its attributes are given an index value. 
        for item, task in enumerate(tasks_list):
            # If the given task ID matches a task ID in the task list, 
            # the chosen list item (task) and all its attributes is deleted.
            if task.task_id == task_id:
                del tasks_list[item]
                # Prints message back to the user that the chosen task has been successfully deleted.
                print(f"Task {task_id} deleted successfully.")
            else:
                # If the task ID given does not match a task ID in the list, the user is notified.
                print(f"Task ID {task_id} not found.")

    def list_tasks():
        """ All outstanding task items are listed along with their ID, 
        task description and completion date"""
        print("Your outstanding tasks are:")
        for task in tasks_list:
            print(f"{task.task_id}, '{task.task_description}' Complete this task by {task.completion_date}.")
        print()

# Example tasks added to list.
tasks_list = [
    Task(1, "Pick up dry cleaning.", "31/05/24"),
    Task(2, "File taxes", "14/06/25"),
    Task(3, "Book nail appointment.", "01/06/24"),
] 

Task.list_tasks()
