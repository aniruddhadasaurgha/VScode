from tkinter import *
import random
import time
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import tkinter as tk
import string

def rock_paper_scissor():
    choices = ['Rock', 'Paper', 'Scissor']
    user_score = 0
    computer_score = 0
    rounds = 5

    def play_round():
        nonlocal user_score, computer_score
        user_choice = simpledialog.askstring("Input", "Enter Rock, Paper, or Scissor:")
        if not user_choice:
            messagebox.showinfo("Cancelled", "Round cancelled.")
            return

        user_choice = user_choice.strip().capitalize()
        if user_choice not in choices:
            messagebox.showerror("Error", "Invalid choice! Please choose Rock, Paper, or Scissor.")
            return

        computer_choice = random.choice(choices)
        result = ""

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif ((user_choice == 'Rock' and computer_choice == 'Scissor') or
              (user_choice == 'Paper' and computer_choice == 'Rock') or
              (user_choice == 'Scissor' and computer_choice == 'Paper')):
            user_score += 1
            result = "You win this round!"
        else:
            computer_score += 1
            result = "Computer wins this round!"

        messagebox.showinfo("Round Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}\n\nScores:\nYou: {user_score}\nComputer: {computer_score}")

    for _ in range(rounds):
        play_round()

    if user_score > computer_score:
        final_result = "Congratulations! You won the game!"
    elif user_score < computer_score:
        final_result = "Computer wins the game! Better luck next time."
    else:
        final_result = "The game is a tie!"
    messagebox.showinfo("Game Over", f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}\n\n{final_result}")

if __name__ == "__main__":
    root = Tk()
    root.title("Rock Paper Scissor Game")
    root.geometry("400x300")
    start_button = Button(root, text="Start Game", command=rock_paper_scissor, font=("Arial", 16), bg="blue", fg="white")
    start_button.pack(pady=100)
    root.mainloop()



