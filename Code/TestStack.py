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
    random.shuffle(memeList)
    return memeList


def get_random_meme(memeList, seenList, label, check=False):
    if check == False:
        meme = memeList.pop(0)
        meme_img = ImageTk.PhotoImage(Image.open(meme))
        label.config(image=meme_img)
        label.image = meme_img # Keep a reference to the image object
        print('forward', meme)
        seenList.insert(0, meme)
    else:
        meme = seenList.pop(0)
        meme_img = ImageTk.PhotoImage(Image.open(meme))
        label.config(image=meme_img)
        label.image = meme_img
        print('backward', meme)
        memeList.insert(0, meme)

if __name__ == "__main__":
    window = Tk()
    window.title('Meme Dealers')
    window.geometry('1500x800')

    welcome_img = ImageTk.PhotoImage(Image.open('Welcome.jpg'))
    image_label = Label(window, image=welcome_img)
    image_label.pack()

    memes = load_memes()
    seen = []
    btn = Button(window, text='Get Meme', command=lambda: get_random_meme(memes, seen, image_label))
    backbtn = Button(window, text='Last Meme', command=lambda: get_random_meme(memes, seen, image_label, True))
    btn.pack()
    backbtn.pack()

    window.mainloop()
