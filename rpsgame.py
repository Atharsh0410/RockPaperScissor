import tkinter as tk
import random

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def make_choice(choice):
    global user_score, computer_score
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = check_winner(choice, computer_choice)
    result_label.config(text=f"You chose {choice.capitalize()}. Computer chose {computer_choice.capitalize()}. {result}")
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    update_scores()
    if user_score == 5 or computer_score == 5:
        end_game()

def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def end_game():
    if user_score > computer_score:
        winner_label.config(text="You win the game!")
    else:
        winner_label.config(text="Computer wins the game!")

    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

#tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")


user_score = 0
computer_score = 0
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)
user_score_label = tk.Label(root, text="Your Score: 0", font=("Helvetica", 12))
user_score_label.pack()
computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Helvetica", 12))
computer_score_label.pack()
winner_label = tk.Label(root, text="", font=("Helvetica", 16))
winner_label.pack(pady=10)

# Buttons
rock_button = tk.Button(root, text="Rock", command=lambda: make_choice("rock"))
rock_button.pack(side=tk.LEFT, padx=10)
paper_button = tk.Button(root, text="Paper", command=lambda: make_choice("paper"))
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button = tk.Button(root, text="Scissors", command=lambda: make_choice("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
