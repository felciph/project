import tkinter as tk
from tkinter import font

# List of questions and corresponding labels
questions = [
    ("Rate your mental health out of 5:", 
     ["1 - Awful", "2 - Bad", "3 - Ordinary", "4 - Good", "5 - Excellent"]),
    
    ("What's your time management skills?", 
     ["1 - Awful", "2 - Bad", "3 - Ordinary", "4 - Good", "5 - Excellent"]),
    
    ("Rate your productivity level:", 
     ["1 - Awful", "2 - Bad", "3 - Ordinary", "4 - Good", "5 - Excellent"]),
    
    ("What are your hobbies?", ),
    
    ("How long do you usually study in weekdays?", 
     ["• 0-1 hour", "• 1-3 hours", "• 3+ hours"]),
    
    ("How long do you usually study in weekends?", 
     ["• 0-1 hour", "• 1-3 hours", "• 3+ hours"]),
    
    ("Do you have anyone to lean on when things get tough?", 
     ["Yes 😀", "No 🙁"]),
]

# Dictionary to store user responses
responses = {}

question_index = 0  # Track the current question
label_widgets = []  # Store label widgets for easy update

def next_question(event=None):
    global question_index
    user_answer = entry.get()  # Get user input
    if user_answer:  # Store the answer only if the user has entered something
        responses[questions[question_index][0]] = user_answer
    entry.delete(0, tk.END)  # Clear input box for the next question

    # Move to the next question if available
    if question_index < len(questions) - 1:
        question_index += 1
        update_question()
    else:
        # Display a thank-you message after the last question
        label_question.config(text="Thank you for the information. This will help us optimize your experience on this app!")
        entry.pack_forget()  # Hide the input box
        button_next.pack_forget()  # Hide the button
        for lbl in label_widgets:
            lbl.pack_forget()  # Hide all answer labels
        print(responses)  # Print the stored responses to the console (optional)

def update_question():
    # Update question text
    label_question.config(text=questions[question_index][0])
    
    # Remove old labels
    for lbl in label_widgets:
        lbl.destroy()
    label_widgets.clear()

    # Add new labels **BEFORE** packing the entry box and button
    if len(questions[question_index]) > 1:
        for text in questions[question_index][1]:
            lbl = tk.Label(frame_labels, text=text, font=("Segoe UI", 12), fg="#333333", bg="#F4F4F9", pady=10)
            lbl.pack(anchor="w", padx=20)  # Align labels to the left with some padding
            label_widgets.append(lbl)

# Create the main window
root = tk.Tk()
root.title("Breathe")  # Window title
root.geometry("1280x720")  # Default resolution

# Create a Canvas for the dynamic background
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack(fill="both", expand=True)

# Function to draw the gradient background dynamically
def draw_gradient(event=None):
    canvas.delete("gradient")  # Clear previous gradient
    width, height = root.winfo_width(), root.winfo_height()

    # Create a smooth gradient effect
    for i in range(height):
        color = f"#{int(168 + (255 - 168) * (i / height)):02X}DADC"  # Gradient from #A8DADC to white
        canvas.create_line(0, i, width, i, fill=color, tags="gradient")

# Bind the resizing event
root.bind("<Configure>", draw_gradient)

# Create a frame to hold the content (now semi-transparent)
content_frame = tk.Frame(root, bg="#F4F4F9", bd=0)
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a header label for the first question
label_question = tk.Label(content_frame, text=questions[question_index][0], font=("Segoe UI", 18, "bold"), fg="#1D1D1D", bg="#F4F4F9")
label_question.pack(pady=20)

# Create a frame to hold the labels (ensures labels stay together)
frame_labels = tk.Frame(content_frame, bg="#F4F4F9")
frame_labels.pack(pady=10)

# Add initial labels
update_question()  # Call the function once to set up the first question

# Create an entry widget (text input box)
entry = tk.Entry(content_frame, width=30, font=("Segoe UI", 14), relief="solid", bd=2, bg="#FFFFFF", fg="#333333")
entry.pack(pady=20)

# Bind the Enter key to the next_question function
root.bind("<Return>", next_question)

# Create a custom button style
button_next = tk.Button(content_frame, text="Next", command=next_question, font=("Segoe UI", 14, "bold"), fg="#FFFFFF", bg="#4CAF50", relief="flat", width=20, height=2)
button_next.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
