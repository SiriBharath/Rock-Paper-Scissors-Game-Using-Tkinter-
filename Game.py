import tkinter as tk
import random

# Define the game logic
def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if user_choice == computer_choice:
        outcome = "Tie"
    elif user_choice == "rock" and computer_choice == "scissors" or \
         user_choice == "paper" and computer_choice == "rock" or \
         user_choice == "scissors" and computer_choice == "paper":
        outcome = "You win!"
    else:
        outcome = "Computer wins!"
    return computer_choice, outcome

# Define the GUI
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the choice buttons
rock_button = tk.Button(root, text="Rock", width=10)
paper_button = tk.Button(root, text="Paper", width=10)
scissors_button = tk.Button(root, text="Scissors", width=10)

# Add the choice buttons to the GUI
rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

# Define the button click handlers
def on_rock_click():
    computer_choice, outcome = play_game("rock")
    update_display(computer_choice, outcome)

def on_paper_click():
    computer_choice, outcome = play_game("paper")
    update_display(computer_choice, outcome)

def on_scissors_click():
    computer_choice, outcome = play_game("scissors")
    update_display(computer_choice, outcome)

# Add the button click handlers
rock_button.config(command=on_rock_click)
paper_button.config(command=on_paper_click)
scissors_button.config(command=on_scissors_click)

# Create the label to display the computer's choice and outcome
display_label = tk.Label(root, text="", font=("Arial", 6), pady=20)
display_label.pack()

# Define the function to update the label with the computer's choice and outcome
def update_display(computer_choice, outcome):
    display_label.config(text=f"Computer chose {computer_choice}. {outcome}")

# Start the GUI event loop
root.mainloop()
