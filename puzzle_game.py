import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import PhotoImage
from piece_maker import nine_piecer

# create main class for the game itself
class PuzzleGame:
    # function to create the window
    def __init__(self, title, width, height):
        # don't fully understand the init and self stuff
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        # cutting up the image into 9 pieces
        self.pieces = nine_piecer("bird.jpg")

        # removing one piece
        blank_piece = None
        random_index = random.randint(0, 8)
        self.pieces[random_index] = blank_piece

        # randomize order by shuffling
        random.shuffle(self.pieces)

        # creating buttons in which we will put our pieces
        index = 0
        self.buttons = []
        self.photos = []
        for i in range(0, 600, 200):
            for j in range(0, 600, 200):
                if index < len(self.pieces):

                    piece = self.pieces[index]

                    if piece is None:
                        blank_img = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
                        photo = ImageTk.PhotoImage(blank_img)
                    else:
                        photo = ImageTk.PhotoImage(piece)

                    # create button with the image
                    button = tk.Button(self.window, image=photo)
                    button.image = photo
                    button.place(x=i, y=j)

                    # store button
                    self.buttons.append(button)

                    index += 1

    # interaction with buttons add later

    # function to run the game
    def run(self):
        self.window.mainloop()

# creating instance of the game
game = PuzzleGame("Puzzle Game!", 600, 600)
game.run()