import tkinter as tk
from tkinter import messagebox
import random

class ProductivityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Productivity App")

        self.tasks = [
            "Read a chapter from a book",
            "Plan your tasks for the day",
            "Practice a new language",
            "Exercise for 30 minutes",
            "Learn a new recipe and cook it"
            # Add more tasks
        ]

        self.completed_tasks = []

        self.current_task_index = None  # Initialize to None

        self.root.configure(bg="#222")  # Set background color

        self.task_label = tk.Label(root, text="Random Task:", font=("Helvetica", 16), bg="#222", fg="white")
        self.task_label.pack(pady=20)

        self.generate_task_button = tk.Button(root, text="Generate Task", command=self.generate_task, font=("Helvetica", 14), bg="#333", fg="white")
        self.generate_task_button.pack(pady=10)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=("Helvetica", 14), bg="#28a745", fg="white")
        self.complete_task_button.pack(pady=10)
        self.complete_task_button["state"] = "disabled"  # Initially disabled

        self.add_custom_task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.add_custom_task_entry.pack(pady=10)

        self.add_custom_task_button = tk.Button(root, text="Add Custom Task", command=self.add_custom_task, font=("Helvetica", 14), bg="#ffc107", fg="white")
        self.add_custom_task_button.pack(pady=10)

        self.completed_tasks_label = tk.Label(root, text="Completed Tasks:", font=("Helvetica", 16), bg="#222", fg="white")
        self.completed_tasks_label.pack(pady=20)

        self.completed_tasks_text = tk.Text(root, height=10, width=40, font=("Helvetica", 12))
        self.completed_tasks_text.pack()
        
    def generate_task(self):
        if not self.tasks:
            self.task_label.config(text="No tasks left!")
            self.complete_task_button["state"] = "disabled"
        else:
            self.current_task_index = random.randint(0, len(self.tasks) - 1)
            random_task = self.tasks[self.current_task_index]
            self.task_label.config(text="Random Task: " + random_task)
            self.complete_task_button["state"] = "normal"

    def complete_task(self):
        if self.current_task_index is not None:
            selected_task = self.tasks[self.current_task_index]
            self.mark_task_completed(selected_task)
            self.generate_task()
        else:
            messagebox.showwarning("No Task", "Generate a task before completing.")
        
    def add_custom_task(self):
        custom_task = self.add_custom_task_entry.get()
        if custom_task:
            self.tasks.append(custom_task)
            self.add_custom_task_entry.delete(0, tk.END)
            messagebox.showinfo("Custom Task Added", "Custom task added successfully!")
        else:
            messagebox.showwarning("Empty Task", "Please enter a custom task.")
            
    def show_completed_tasks(self):
        self.completed_tasks_text.delete(1.0, tk.END)
        for task in self.completed_tasks:
            self.completed_tasks_text.insert(tk.END, f"- {task}\n")
            
    def mark_task_completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed_tasks.append(task)
            self.show_completed_tasks()  # Update completed tasks in the text area
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ProductivityApp(root)
    root.mainloop()
