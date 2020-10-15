import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

label1 = tkinter.Label(root, text = "")
label1.pack()

label2 = tkinter.Label(root, text = "Hello to you!", fg = "light green", bg = "dark green", font = "Helvetica 16 bold italic")
label2.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label2 = tkinter.Label(root, image = image1)
label2.image = image1
label2.pack(expand = True)

def rolling_dice():
	image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
	label2.configure(image=image1)
	label2.image = image1

button = tkinter.Button(root, text = 'Roll the Dice', fg = 'blue', command = rolling_dice)

button.pack(expand = True)

root.mainloop()
