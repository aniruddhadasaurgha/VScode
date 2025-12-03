import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissor"]

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text=f"Player: {user_choice}")
    comp_label.config(text=f"Computer: {computer_choice}")

    
    if user_choice == computer_choice:
        result_label.config(text="Result: It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        result_label.config(text="Result: You Win!")
    else:
        result_label.config(text="Result: Computer Wins!")

def reset_game():
    user_label.config(text="Player: ")
    comp_label.config(text="Computer: ")
    result_label.config(text="Result: ")


root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x300")


user_label = tk.Label(root, text="Player: ", font=("Arial", 14))
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer: ", font=("Arial", 14))
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"))
result_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissor", width=10, command=lambda: play("Scissor")).grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="Restart Game", width=15, command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
