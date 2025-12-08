"""
File: smith_todo.py
Author: Johnathan Smith
Course: CSD-325
Module: 10
Description:
    Tkinter scrolling To-Do list application based on Listing 2.2
    with the following modifications:
      - Window title set to "Smith-ToDo"
      - Menu items use complementary colors
      - Tasks are deleted with RIGHT mouse button instead of LEFT
      - Label explains how to delete a task
      - File -> Exit menu item added to close the program
"""

import tkinter as tk


def add_task():
    """Add the text from the entry box as a new task."""
    task_text = task_entry.get().strip()
    if task_text:
        todo_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)


def delete_task_by_event(event):
    """
    Delete the task that is right-clicked in the listbox.
    Uses the y-coordinate of the mouse to find the nearest item.
    """
    index = todo_listbox.nearest(event.y)
    if index >= 0:
        todo_listbox.delete(index)


def delete_selected_task():
    """Delete the currently selected task (used by the menu)."""
    selection = todo_listbox.curselection()
    if selection:
        todo_listbox.delete(selection[0])


def exit_program():
    """Exit the application cleanly."""
    root.destroy()


# --- main window setup ---
root = tk.Tk()
root.title("Smith-ToDo")  # required change: lastname-ToDo
root.geometry("400x300")

# --- menu bar setup ---
menubar = tk.Menu(root)

# File menu (with Exit)
file_menu = tk.Menu(
    menubar,
    tearoff=0,
    bg="#1f2933",  # dark slate
    fg="#f9fafb"   # near white
)
file_menu.add_command(label="Exit", command=exit_program)
menubar.add_cascade(label="File", menu=file_menu)

# Tasks menu (secondary color)
tasks_menu = tk.Menu(
    menubar,
    tearoff=0,
    bg="#fbbf24",  # warm amber
    fg="#111827"   # dark text
)
tasks_menu.add_command(label="Add Task", command=add_task)
tasks_menu.add_command(label="Delete Selected Task", command=delete_selected_task)
menubar.add_cascade(label="Tasks", menu=tasks_menu)

root.config(menu=menubar)

# --- main frame for listbox + scrollbar ---
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

todo_listbox = tk.Listbox(main_frame, height=10)
todo_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# connect scrollbar and listbox
todo_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todo_listbox.yview)

# bind RIGHT mouse button to delete
# (on most platforms <Button-3> is the right mouse button)
todo_listbox.bind("<Button-3>", delete_task_by_event)

# --- entry and add button ---
entry_frame = tk.Frame(root)
entry_frame.pack(fill=tk.X, padx=10, pady=(0, 5))

task_entry = tk.Entry(entry_frame)
task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

# --- instruction label ---
instruction_label = tk.Label(
    root,
    text="Tip: Add tasks above, then RIGHT-click a task to delete it.",
    anchor="w"
)
instruction_label.pack(fill=tk.X, padx=10, pady=(0, 10))

# start the Tkinter event loop
root.mainloop()
