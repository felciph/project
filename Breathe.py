import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Breathe - Wellness Tracker")
root.geometry("1280x720")  # You can change this to any resolution
root.resizable(True, True)

# ====== Left Sidebar Navigation (with Scrollbar) ======
# Create a canvas for scrolling
canvas = tk.Canvas(root, bg="#2C3E50", width=250, height=720)
canvas.pack(side="left", fill="y", padx=(10, 0))

# Add a scrollbar to the canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="left", fill="y")

# Configure canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the navigation buttons
nav_bar_frame = tk.Frame(canvas, bg="#2C3E50", width=250)
canvas.create_window((0, 0), window=nav_bar_frame, anchor="nw")

# Add buttons to the navigation bar
nav_buttons = [
    ("🏠 Home", lambda: show_frame(home_frame)),
    ("📋 Survey", lambda: show_frame(survey_frame)),
    ("⚙️ Settings", lambda: show_frame(settings_frame)),
    ("📝 To do list", lambda: show_frame(todo_frame)),
    ("🎶 Sound Library", lambda: show_frame(sound_frame)),
    ("🧘‍♀️ Meditation", lambda: show_frame(meditation_frame)),
    ("🤖 Aeolus Ai", lambda: show_frame(aeolus_ai_frame)),
]

# Add navigation buttons to the frame with equal height for each button
for text, command in nav_buttons:
    btn = tk.Button(nav_bar_frame, text=text, font=("Segoe UI", 14), fg="white", bg="#34495E", relief="flat", height=3, command=command)
    btn.pack(fill="x", pady=10)

# Update the canvas scroll region to encompass all buttons
nav_bar_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# ====== Main Content Frame ======
main_frame = tk.Frame(root, bg="#F4F4F9", width=1030, height=720)
main_frame.pack(side="right", fill="both", expand=True)

# ====== Function to Show Selected Page ======
def show_frame(frame):
    """Hides all frames and only shows the selected one."""
    for f in [home_frame, survey_frame, settings_frame, todo_frame, sound_frame, meditation_frame, aeolus_ai_frame]:
        f.pack_forget()
    frame.pack(fill="both", expand=True)

# ====== Home Page ======
home_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(home_frame, text="🌿 Welcome to Breathe!", font=("Segoe UI", 22, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(home_frame, text="Your personal wellness tracker to help you stay balanced.", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# ====== Survey Page ======
survey_frame = tk.Frame(main_frame, bg="#F4F4F9")

questions = [
    ("Rate your mental health out of 5:", ["1", "2", "3", "4", "5"]),
    ("What's your time management skill?", ["1", "2", "3", "4", "5"]),
    ("Rate your productivity level:", ["1", "2", "3", "4", "5"]),
    ("What are your hobbies", None),
    ("How long do you usually study in weekdays?", ["• 0-1 hour", "• 1-3 hours", "• 3+ hours"]),
    ("How long do you usually study in weekends?", ["• 0-1 hour", "• 1-3 hours", "• 3+ hours"]),
    ("Do you have anyone to lean on when things get tough?", ["Yes", "No"]),
]

responses = {}
question_index = 0
label_widgets = []

def next_question(event=None):
    """Moves to the next survey question and updates the display."""
    global question_index
    user_answer = entry.get()
    
    # Validate user input based on the current question
    if validate_input(user_answer):
        responses[questions[question_index][0]] = user_answer
        entry.delete(0, tk.END)

        if question_index < len(questions) - 1:
            question_index += 1
            update_question()
        else:
            label_question.config(text="Thank you for your responses! Your answers help us improve your experience.")
            entry.pack_forget()
            button_next.pack_forget()
            for lbl in label_widgets:
                lbl.pack_forget()
    else:
        # Show a message box if input is invalid
        messagebox.showwarning("Invalid input", "Please enter a valid response.")

def validate_input(user_input):
    """Validates the input based on the question."""
    current_question = questions[question_index][0]
    
    if current_question in ["Rate your mental health out of 5:", "What's your time management skill?", "Rate your productivity level:"]:
        if user_input.isdigit() and int(user_input) in [1, 2, 3, 4, 5]:
            return True
        return False
    
    if current_question in ["How long do you usually study in weekdays?", "How long do you usually study in weekends?"]:
        valid_options = ["• 0-1 hour", "• 1-3 hours", "• 3+ hours"]
        if user_input in valid_options:
            return True
        return False
    
    if current_question == "Do you have anyone to lean on when things get tough?":
        if user_input.lower() in ["yes", "no"]:
            return True
        return False
    
    if current_question == "What are your hobbies":
        if len(user_input.strip()) > 0:
            return True
        return False

    return False

def update_question():
    """Updates the question text and response options."""
    label_question.config(text=questions[question_index][0])

    for lbl in label_widgets:
        lbl.destroy()
    label_widgets.clear()

    entry.pack_forget()
    button_next.pack_forget()

    if len(questions[question_index]) > 1:
        for text in questions[question_index][1]:
            lbl = tk.Label(survey_frame, text=text, font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9")
            lbl.pack(pady=5)
            label_widgets.append(lbl)

    entry.pack(pady=10)
    button_next.pack(pady=20)

label_question = tk.Label(survey_frame, text=questions[question_index][0], font=("Segoe UI", 16, "bold"), fg="#1D1D1D", bg="#F4F4F9")
label_question.pack(pady=20)

entry = tk.Entry(survey_frame, width=30, font=("Segoe UI", 14), relief="solid", bd=1, bg="#FFFFFF", fg="#333333", justify="center")
button_next = tk.Button(survey_frame, text="Next", command=next_question, font=("Segoe UI", 14, "bold"), fg="white", bg="#4CAF50", relief="flat", width=20, height=2)

root.bind("<Return>", next_question)

update_question()

# ====== Settings Page ======
settings_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(settings_frame, text="⚙️ Settings", font=("Segoe UI", 18, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(settings_frame, text="Customize your experience here.", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# ====== To Do List Page ======
todo_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(todo_frame, text="📝 To Do List", font=("Segoe UI", 22, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(todo_frame, text="Organize your tasks here!", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# ====== Sound Library Page ======
sound_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(sound_frame, text="🎶 Sound Library", font=("Segoe UI", 22, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(sound_frame, text="Relaxing sounds to accompany you.", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# ====== Meditation Page ======
meditation_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(meditation_frame, text="🧘‍♀️ Meditation", font=("Segoe UI", 22, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(meditation_frame, text="Relax and meditate!", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# ====== Aeolus AI Page ======
aeolus_ai_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(aeolus_ai_frame, text="🤖 Aeolus AI", font=("Segoe UI", 22, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(aeolus_ai_frame, text="Let Aeolus assist with your wellness journey.", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# Show Home Page Initially
show_frame(home_frame)

root.mainloop()
