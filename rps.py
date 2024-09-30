import tkinter as tk
from random import choice
from PIL import Image, ImageTk

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("600x500") 

        self.your_score = 0
        self.computer_score = 0

        self.your_score_label = tk.Label(self.window, text="Your Score: 0", font=("Arial", 20))
        self.your_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0", font=("Arial", 20))
        self.computer_score_label.pack()

        self.your_choice_label = tk.Label(self.window, text="", font=("Arial", 20))
        self.your_choice_label.pack()

        self.computer_choice_label = tk.Label(self.window, text="", font=("Arial", 20))
        self.computer_choice_label.pack()

        self.computer_choice_image_label = tk.Label(self.window, image=None)
        self.computer_choice_image_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 20))
        self.result_label.pack()

        # Load and resize images
        self.rock_image = Image.open("rock.png")
        self.rock_image = self.rock_image.resize((50, 50))  # Resize to 50x50 pixels
        self.rock_image = ImageTk.PhotoImage(self.rock_image)

        self.paper_image = Image.open("paper.png")
        self.paper_image = self.paper_image.resize((50, 50))  # Resize to 50x50 pixels
        self.paper_image = ImageTk.PhotoImage(self.paper_image)

        self.scissors_image = Image.open("scissors.png")
        self.scissors_image = self.scissors_image.resize((50, 50))  # Resize to 50x50 pixels
        self.scissors_image = ImageTk.PhotoImage(self.scissors_image)

        # Create buttons with images
        self.rock_button = tk.Button(self.window, image=self.rock_image, command=lambda: self.play("rock"))
        self.rock_button.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

        self.paper_button = tk.Button(self.window, image=self.paper_image, command=lambda: self.play("paper"))
        self.paper_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.scissors_button = tk.Button(self.window, image=self.scissors_image, command=lambda: self.play("scissors"))
        self.scissors_button.place(relx=0.75, rely=0.6, anchor=tk.CENTER)

    def play(self, your_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)

        if your_choice == computer_choice:
            result = "It's a tie!"
        elif (your_choice == "rock" and computer_choice == "scissors") or \
             (your_choice == "paper" and computer_choice == "rock") or \
             (your_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.your_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        # Update your's and computer's choice labels
        self.computer_choice_label['text'] = f"Computer:"
        if computer_choice == "rock":
            self.computer_choice_image_label['image'] = self.rock_image
        elif computer_choice == "paper":
            self.computer_choice_image_label['image'] = self.paper_image
        elif computer_choice == "scissors":
            self.computer_choice_image_label['image'] = self.scissors_image
        self.computer_choice_image_label.image = self.computer_choice_image_label['image']

        self.result_label['text'] = result
        self.your_score_label['text'] = f"Your Score: {self.your_score}"
        self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()