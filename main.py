import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Breathe - Mindfulness App")
root.geometry("800x600")

# Style configuration
style = ttk.Style()
style.configure('leftpane.TFrame', background='#E6F2E2')  # Sidebar color
style.configure('content.TFrame', background='#9AB1C8')  # Background color

# Button Styles
style.configure("TButton",
                padding=10,
                relief="flat",
                background="#4CAF50",  # Green color
                font=("Arial", 12, "bold"),
                foreground="black")
style.map("TButton",
          background=[('active', '#45a049')])  # Darker green when hovered

# Checkbutton Styles
style.configure("TCheckbutton",
                font=("Arial", 12),
                background="#9AB1C8",
                padding=5,
                foreground="black")
style.map("TCheckbutton",
          background=[('active', '#7b8f8e')])  # Light grey when hovered

# Left pane
left_pane = ttk.Frame(root, width=200, style='leftpane.TFrame')
left_pane.pack(side=tk.LEFT, fill=tk.Y)

# Content pane
content_pane = ttk.Frame(root, style='content.TFrame')
content_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Menu items
menu_items = [
    ("Mindfulness Exercises", lambda: display_content("Mindfulness Exercises")),
    ("Relaxation Techniques", lambda: display_content("Relaxation Techniques")),
    ("Stress Relief Tips", lambda: display_content("Stress Relief Tips")),
    ("Customize Settings", lambda: display_content("Customize Settings")),
    ("About", lambda: display_content("About")),
    ("To-do list", lambda: display_content("To-do list"))  # To-do list button
]

for text, command in menu_items:
    btn = ttk.Button(left_pane, text=text, command=command)
    btn.pack(fill=tk.X, padx=10, pady=5)

# Function to display content
def display_content(title):
    # Clear previous content in the content pane
    for widget in content_pane.winfo_children():
        widget.destroy()

    if title == "To-do list":
        show_todo_list()
    else:
        # Use a smoother font with anti-aliasing
        label = ttk.Label(content_pane, text=f"Welcome to {title}", font=("Helvetica Neue", 18, "bold"))
        label.pack(pady=20)

        description = {
            "Mindfulness Exercises": "Engage in a series of tailored exercises designed to enhance your mindfulness and bring a sense of calm and focus to your day.",
            "Relaxation Techniques": "Explore various techniques aimed at helping you unwind and manage stress effectively.",
            "Stress Relief Tips": "Discover practical tips and tricks for reducing stress and improving your overall well-being.",
            "Customize Settings": "Adjust settings to personalize your mindfulness journey.",
            "About": "Learn more about the Breathe app and its creators."
        }

        # Use a larger font for description to enhance readability
        desc_label = ttk.Label(content_pane, text=description[title], wraplength=600, font=("Arial", 12))
        desc_label.pack(pady=10)

# Function to display the to-do list in checklist style
def show_todo_list():
    # Title for To-Do List
    label = ttk.Label(content_pane, text="Your To-Do List", font=("Helvetica Neue", 18, "bold"))
    label.pack(pady=20)

    # Create the entry widget for adding to-do items
    todo_entry = ttk.Entry(content_pane, width=50, font=("Arial", 12))
    todo_entry.pack(pady=10)

    # List to store to-do items and their checkbox states
    todo_items = []
    todo_checkbuttons = []

    # Create a frame to contain all tasks (the singular box around tasks)
    task_container = ttk.Frame(content_pane, padding=10, relief="solid", borderwidth=1)
    task_container.pack(fill=tk.BOTH, padx=20, pady=8)

    # Function to add item to the checklist
    def add_todo_item():
        item = todo_entry.get()
        if item:
            var = tk.BooleanVar(value=False)  # Variable to track the checkbox state (done or not)
            todo_items.append((item, var))

            # Create a frame for each task inside the container
            task_frame = ttk.Frame(task_container, padding=5, relief="flat")
            task_frame.pack(fill=tk.X, padx=10, pady=5)

            # Create a checkbutton for each item added inside the task frame
            checkbutton = ttk.Checkbutton(task_frame, text=item, variable=var, style="TCheckbutton", command=lambda: check_item(var, item, task_frame))
            checkbutton.pack(side=tk.LEFT, padx=10)

            todo_checkbuttons.append(checkbutton)

            todo_entry.delete(0, tk.END)

    # Function to remove item automatically after 1 second if checked
    def check_item(var, item, task_frame):
        if var.get():  # If the checkbox is checked
            # Simulate removal after 1 second
            task_frame.after(1000, task_frame.destroy)

    # Button to add item to the to-do list
    add_button = ttk.Button(content_pane, text="Add Item", command=add_todo_item)
    add_button.pack(pady=15)

# Initial content display
display_content("Mindfulness Exercises")

# Run the application
root.mainloop()
