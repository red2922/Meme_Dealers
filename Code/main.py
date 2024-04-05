from tkinter import *
from PIL import ImageTk, Image
import random
import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from open_api import ImageGenerate
import webbrowser

def load_memes(dir):
    memeList = []
    for meme in os.listdir(dir):
        filePath = dir + meme # Directory attached to filename for easy getting
        memeList.append(filePath)
    random.shuffle(memeList)
    return memeList


def resize_img(img):
    height = 500
    height_rate = height / float(img.size[1])
    width = int(float(img.size[0]) * float(height_rate))
    return img.resize((width, height))


def get_random_meme(memeList, seenList, check, label):
    check[0] = 0
    meme = memeList.pop(0)
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme_resized)
    label.image = meme_resized  # Keep a reference to the image object
    seenList.insert(0, meme)
    print(str(meme))
    return meme


def last_meme(memeList, seenList, check, label):
    check[0] = 1
    meme = seenList.pop(0)
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme_resized)
    label.image = meme_resized
    memeList.insert(0, meme)
    return meme


def toggle():
    global og
    if og:
        toggle_btn.config(image=toggle_ai_face)
        og = False
    else:
        toggle_btn.config(image=toggle_og_face)
        og = True

def share(check):
    #webbrowser.open("https://twitter.com/home")


    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    #options.add_argument("-profile", "")
    driver.get("https://twitter.com/home")
    """"""
    if check[0] == 0:
        meme = last_meme(memes, meme_seen, back_forward_check, image_label)
    else:
        meme = get_random_meme(memes, meme_seen, back_forward_check, image_label)
    print(meme)

def set_file_name(prompt):
    return prompt.split()[6] + ".png"

def generate_and_show(connect: ImageGenerate, prompt: str, window: Tk):
    connect.set_prompt(prompt)
    file_name = set_file_name(prompt)
    direct = "AI_Memes/" + file_name

    connect.generateImage()
    connect.saveImage(direct)

    new = Toplevel(window)
    new.title(file_name)
    new.geometry("1352x878")

    new_Image = Image.open(direct)
    ai_image = ImageTk.PhotoImage(resize_img(new_Image))
    Label(new, image=ai_image).pack()
    new.mainloop()


if __name__ == "__main__":
    global og

    meme_dir = 'Memes for Meme God/'
    ai_dir = 'AI_Memes/'
    initial = "Make me a meme of a dog"
    meme_seen = []
    ai_seen = []
    back_forward_check = [0]
    og = True

    generate = ImageGenerate(initial)

    window = Tk()
    window.title('Meme Dealers')
    window.geometry('1352x878')

    welcome_img = Image.open('Welcome.jpg')
    welcome = ImageTk.PhotoImage(resize_img(welcome_img))
    image_label = Label(window, image=welcome)
    image_label.pack()

    memes = load_memes(meme_dir)
    ai_memes = load_memes(ai_dir)
    
    btn = Button(window, text='Get Meme', command=lambda: get_random_meme(memes, meme_seen, back_forward_check, image_label) if og == True else get_random_meme(ai_memes, ai_seen, image_label))
    backbtn = Button(window, text='Last Meme', command=lambda: last_meme(memes, meme_seen, back_forward_check, image_label) if og == True else last_meme(ai_memes, ai_seen, image_label))
    btn.pack(ipady=10)
    backbtn.pack(ipady=10)

    gene_btn = Button(window, text="Generate Meme", command=lambda: generate_and_show(generate, initial, window))
    gene_btn.pack(ipady=10)

    share_btn = Button(window, text='Share', command=lambda: share(back_forward_check))
    share_btn.pack(ipady=10)

    toggle_og_face = ImageTk.PhotoImage(Image.open("toggle_og.jpg"))
    toggle_ai_face = ImageTk.PhotoImage(Image.open("toggle_ai.jpg"))
    toggle_btn = Button(window, image=toggle_og_face, command=lambda: toggle())
    toggle_btn.pack()

    window.mainloop()
