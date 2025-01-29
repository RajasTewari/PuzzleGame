import tkinter
# importing grid_maker function
from piece_maker import nine_piecer

class PuzzleGame:
    def game_window(self):
        window = tkinter.Tk()
        window.title = "Puzzle Game"
        nine_piecer("bird.jpg")
        window.mainloop()