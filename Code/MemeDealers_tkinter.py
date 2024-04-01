from tkinter import *
from PIL import ImageTk, Image
import random
import os


def load_memes():
    dir = 'Memes for Meme God/'
    memeList = []
    for meme in os.listdir(dir):
        filePath = dir + meme # Directory attached to filename for easy getting
        memeList.append(filePath)
    return memeList


def get_random_meme(memeList, label):
    meme = memeList[random.randint(0, len(memeList) - 1)]
    meme_img = ImageTk.PhotoImage(Image.open(meme))
    label.config(image=meme_img)
    label.image = meme_img  # Keep a reference to the image object


if __name__ == "__main__":
    window = Tk()
    window.title('Meme Dealers')
    window.geometry('1500x800')

    welcome_img = ImageTk.PhotoImage(Image.open('Welcome.jpg'))
    image_label = Label(window, image=welcome_img)
    image_label.pack()

    memes = load_memes()
    btn = Button(window, text='Get Meme', command=lambda: get_random_meme(memes, image_label))
    btn.pack()

    window.mainloop()
