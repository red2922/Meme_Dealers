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


def resize_img(img):
    width = 500
    width_rate = width / float(img.size[0])
    height = int(float(img.size[1]) * float(width_rate))
    return img.resize((width, height))

def get_random_meme(memeList, label):
    meme_path = memeList[random.randint(0, len(memeList) - 1)]
    meme_img = Image.open(meme_path)
    meme = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme)
    label.image = meme  # Keep a reference to the image object


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
    btn = Button(window, text='Get Meme', command=lambda: get_random_meme(memes, image_label))
    btn.pack()

    toggle_og_face = ImageTk.PhotoImage(Image.open("toggle_og.jpg"))
    toggle_ai_face = ImageTk.PhotoImage(Image.open("toggle_ai.jpg"))
    toggle_btn = Button(window, image=toggle_og_face, command=lambda: toggle())
    toggle_btn.pack()

    window.mainloop()
