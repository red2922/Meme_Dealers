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


def resize_img(img):
    width = 500
    width_rate = width / float(img.size[0])
    height = int(float(img.size[1]) * float(width_rate))
    return img.resize((width, height))


def get_random_meme(memeList, seenList, label):
    meme = memeList.pop(0)
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme_resized)
    label.image = meme_resized  # Keep a reference to the image object
    seenList.insert(0, meme)


def last_meme(memeList, seenList, label):
    meme = seenList.pop(0)
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme_resized)
    label.image = meme_resized
    memeList.insert(0, meme)
og = True  # initiate toggle state


def toggle():
    global og
    if og:
        toggle_btn.config(image=toggle_ai_face)
        og = False
    else:
        toggle_btn.config(image=toggle_og_face)
        og = True


if __name__ == "__main__":
    window = Tk()
    window.title('Meme Dealers')
    window.geometry('1352x878')

    welcome_img = Image.open('Welcome.jpg')
    welcome = ImageTk.PhotoImage(resize_img(welcome_img))
    image_label = Label(window, image=welcome)
    image_label.pack()

    memes = load_memes()
    seen = []
    btn = Button(window, text='Get Meme', command=lambda: get_random_meme(
        memes, seen, image_label))
    backbtn = Button(window, text='Last Meme', command=lambda: last_meme(
        memes, seen, image_label))
    btn.pack()
    backbtn.pack()

    toggle_og_face = ImageTk.PhotoImage(Image.open("toggle_og.jpg"))
    toggle_ai_face = ImageTk.PhotoImage(Image.open("toggle_ai.jpg"))
    toggle_btn = Button(window, image=toggle_og_face, command=lambda: toggle())
    toggle_btn.pack()

    window.mainloop()
