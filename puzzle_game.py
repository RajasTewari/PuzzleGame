import tkinter as tk
import random
# importing grid_maker function
from piece_maker import nine_piecer

# create main class for the game itself
class PuzzleGame:
    # function to create the window
    def __init__(self, title, width, height):
        # don't fully understand the init and self stuff
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        # creating buttons in which we will put our pieces
        for i in range(0, 600, 200):
            for j in range(0, 600, 200):
                # very confused here
                button = tk.Button(random.choice(nine_piecer("bird.jpg")))
                button.place(x=i, y=j)

    # interaction with buttons
    def button_click(self):
        print("no clue")

    # function to run the game
    def run(self):
        self.window.mainloop()

# creating instance of the game
game = PuzzleGame("Puzzle Game!", 600, 600)
game.run()