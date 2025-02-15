import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Breathe - Mindfulness App")
root.geometry("800x600")

# Style configuration
style = ttk.Style()
style.configure('leftpane.TFrame', background='#2c5e4a')
style.configure('content.TFrame', background='white')

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
    ("About", lambda: display_content("About"))
]

for text, command in menu_items:
    btn = ttk.Button(left_pane, text=text, command=command)
    btn.pack(fill=tk.X, padx=10, pady=5)

# Function to display content
def display_content(title):
    for widget in content_pane.winfo_children():
        widget.destroy()

    label = ttk.Label(content_pane, text=f"Welcome to {title}", font=("Helvetica", 16))
    label.pack(pady=20)

    description = {
        "Mindfulness Exercises": "Engage in a series of tailored exercises designed to enhance your mindfulness and bring a sense of calm and focus to your day.",
        "Relaxation Techniques": "Explore various techniques aimed at helping you unwind and manage stress effectively.",
        "Stress Relief Tips": "Discover practical tips and tricks for reducing stress and improving your overall well-being.",
        "Customize Settings": "Adjust settings to personalize your mindfulness journey.",
        "About": "Learn more about the Breathe app and its creators."
    }

    desc_label = ttk.Label(content_pane, text=description[title], wraplength=600)
    desc_label.pack(pady=10)

# Initial content display
display_content("Mindfulness Exercises")

# Run the application
root.mainloop()
