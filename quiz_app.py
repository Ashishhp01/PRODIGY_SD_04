import tkinter as tk
from tkinter import messagebox

# Quiz Data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used for Android development?",
        "options": ["Python", "Kotlin", "C#", "Swift"],
        "answer": "Kotlin"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "HyperText Markup Language",
            "HighText Machine Language",
            "HyperTool Multi Language",
            "HyperTransfer Machine Language"
        ],
        "answer": "HyperText Markup Language"
    },
    {
        "question": "Which company developed the Windows OS?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "Which data structure uses FIFO principle?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    }
]

# Initialize variables
current_q = 0
score = 0

# Functions
def display_question():
    global current_q
    question_label.config(text=questions[current_q]["question"])
    var.set(None)
    for i in range(4):
        options[i].config(text=questions[current_q]["options"][i])

def next_question():
    global current_q, score
    selected = var.get()
    if selected == "":
        messagebox.showwarning("Warning", "Please select an answer!")
        return

    if questions[current_q]["options"][int(selected)] == questions[current_q]["answer"]:
        score += 1

    current_q += 1
    if current_q < len(questions):
        display_question()
    else:
        show_result()

def show_result():
    result_text = f"🎉 Quiz Completed!\n\nYour Score: {score}/{len(questions)}"
    messagebox.showinfo("Result", result_text)
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("🧠 Quiz App")
root.geometry("500x400")
root.config(bg="#1e1e2e")

title_label = tk.Label(root, text="🧩 Quiz Application", font=("Helvetica", 18, "bold"), bg="#1e1e2e", fg="white")
title_label.pack(pady=15)

question_label = tk.Label(root, text="", font=("Arial", 14), bg="#1e1e2e", fg="white", wraplength=450, justify="center")
question_label.pack(pady=20)

var = tk.StringVar(value="")

options = []
for i in range(4):
    btn = tk.Radiobutton(
        root,
        text="",
        variable=var,
        value=str(i),
        font=("Arial", 12),
        bg="#1e1e2e",
        fg="white",
        activebackground="#4CAF50",
        selectcolor="#2e2e3e"
    )
    btn.pack(anchor="w", padx=80)
    options.append(btn)

next_button = tk.Button(root, text="Next ➡️", font=("Arial", 13, "bold"), bg="#4CAF50", fg="white", command=next_question)
next_button.pack(pady=20)

display_question()
root.mainloop()
