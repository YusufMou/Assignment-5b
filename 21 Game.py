from tkinter import *
import random

#Window
root = Tk()
root.geometry("500x300")
root.title("21 Game")

def start():
	computer1 = random.randint(1,10)
	computer2 = random.randint(1,10)
	computer3 = random.randint(1,10)
	Label(root, text="Computer's Guess: ").grid(row=1, column=1)
	Label(root, text=str(computer1)).grid(row=1, column=2)
	Label(root, text=str(computer2)).grid(row=1, column=3)

start()



root.mainloop()