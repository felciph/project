import tkinter as tk
from tkinter import messagebox
from groq import Groq

# Initialize main window
root = tk.Tk()
root.title("Breathe - Wellness Tracker")
root.geometry("1280x720")
root.resizable(True, True)

# Initialize the Groq API
api_key = "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" 
system_prompt = "You are an AI assistant for an application called 'Breath', an application that helps people relieve stress and manage tasks. Keep your answers short, simple, and somewhat informal."
api = Groq(api_key=api_key)

# ====== Left Sidebar Navigation (with Scrollbar) ======
canvas = tk.Canvas(root, bg="#2C3E50", width=250, height=720)
canvas.pack(side="left", fill="y", padx=(10, 0))

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="left", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

nav_bar_frame = tk.Frame(canvas, bg="#2C3E50", width=250)
canvas.create_window((0, 0), window=nav_bar_frame, anchor="nw")

nav_buttons = [
    ("🏠 Home", lambda: show_frame(home_frame)),
    ("📋 Survey", lambda: show_frame(survey_frame)),
    ("⚙️ Settings", lambda: show_frame(settings_frame)),
    ("📝 To do list", lambda: show_frame(todo_frame)),
    ("🎶 Sound Library", lambda: show_frame(sound_frame)),
    ("🧘‍♀️ Meditation", lambda: show_frame(meditation_frame)),
    ("🤖 Aeolus Ai", lambda: show_frame(aeolus_ai_frame)),
]

for text, command in nav_buttons:
    btn = tk.Button(nav_bar_frame, text=text, font=("Segoe UI", 14), fg="white", bg="#34495E", relief="flat", height=3, command=command)
    btn.pack(fill="x", pady=10)

nav_bar_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# ====== Main Content Frame ======
main_frame = tk.Frame(root, bg="#F4F4F9", width=1030, height=720)
main_frame.pack(side="right", fill="both", expand=True)

# Function to show selected page
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

# ====== Aeolus AI Page ======
aeolus_ai_frame = tk.Frame(main_frame, bg="#F4F4F9")
tk.Label(aeolus_ai_frame, text="🤖 Aeolus AI", font=("Segoe UI", 22, "bold"), fg="#1D1D1D", bg="#F4F4F9").pack(pady=20)
tk.Label(aeolus_ai_frame, text="Let Aeolus assist with your wellness journey.", font=("Segoe UI", 14), fg="#333333", bg="#F4F4F9").pack()

# Create Chat UI
chat_box = tk.Text(aeolus_ai_frame, width=80, height=20, font=("Segoe UI", 12), state="disabled", wrap="word", bg="#E9ECEF", fg="#333333")
chat_box.pack(pady=20)

user_input_field = tk.Entry(aeolus_ai_frame, width=80, font=("Segoe UI", 14), relief="solid", bd=1, bg="#FFFFFF", fg="#333333", justify="center")
user_input_field.pack(pady=10)

def get_ai_response(user_input):
    """Handles sending user input to AI and displaying the response."""
    memory = "User: " + user_input + ", "
    completion = api.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": memory},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content
    return response

def send_message():
    """Send the message and display AI response."""
    user_message = user_input_field.get()
    
    if not user_message.strip():
        return
    
    chat_box.config(state="normal")
    chat_box.insert("end", f"You: {user_message}\n")
    chat_box.insert("end", "Aeolus: ...\n")
    chat_box.config(state="disabled")
    
    user_input_field.delete(0, tk.END)

    ai_response = get_ai_response(user_message)

    # Display AI's response
    chat_box.config(state="normal")
    chat_box.delete("end-2l", "end-1l")  # Remove the placeholder text
    chat_box.insert("end", f"Aeolus: {ai_response}\n")
    chat_box.config(state="disabled")
    
    # Auto scroll to the bottom
    chat_box.yview("end")

send_button = tk.Button(aeolus_ai_frame, text="Send", command=send_message, font=("Segoe UI", 14, "bold"), fg="white", bg="#4CAF50", relief="flat", width=20, height=2)
send_button.pack(pady=10)

# ====== Settings, ToDo List, Sound, and Meditation Pages (placeholders) ======
settings_frame = tk.Frame(main_frame, bg="#F4F4F9")
todo_frame = tk.Frame(main_frame, bg="#F4F4F9")
sound_frame = tk.Frame(main_frame, bg="#F4F4F9")
meditation_frame = tk.Frame(main_frame, bg="#F4F4F9")

# Show Home Page Initially
show_frame(home_frame)

root.mainloop()
