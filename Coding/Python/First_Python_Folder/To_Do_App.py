import tkinter as tk

class Task:
    def __init__(self, title: str, status: bool):
        self.title = title
        self.status = status

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.tasks = []

        self.title_label = tk.Label(self.root, text="Your To-Do List", font=("Helvetica", 24))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", font=("Helvetica", 14), command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.complete_task_button = tk.Button(self.root, text="Mark as Complete", font=("Helvetica", 14), command=self.mark_completed)
        self.complete_task_button.pack(pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", font=("Helvetica", 14), command=self.delete_task)
        self.delete_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 14), width=40, height=10)
        self.task_listbox.pack(pady=20)

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title != "":
            new_task = Task(task_title, False)
            self.tasks.append(new_task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks[task_index]
            if not task.status:
                task.status = True
                self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task.status else "Not Completed"
            self.task_listbox.insert(tk.END, f"{task.title} - {status}")

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()