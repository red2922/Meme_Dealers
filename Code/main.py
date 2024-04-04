from tkinter import *
from PIL import ImageTk, Image
import random
import os
from open_api import ImageGenerate


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


def get_random_meme(memeList, seenList, label):
    meme = memeList.pop(0)
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme_resized)
    label.image = meme_resized  # Keep a reference to the image object
    seenList.insert(0, meme)
    print(str(meme))


def last_meme(memeList, seenList, label):
    meme = seenList.pop(0)
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img))
    label.config(image=meme_resized)
    label.image = meme_resized
    memeList.insert(0, meme)


def toggle():
    global og
    if og:
        toggle_btn.config(image=toggle_ai_face)
        og = False
    else:
        toggle_btn.config(image=toggle_og_face)
        og = True


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
    
    btn = Button(window, text='Get Meme', command=lambda: get_random_meme(memes, meme_seen, image_label) if og == True else get_random_meme(ai_memes, ai_seen, image_label))
    backbtn = Button(window, text='Last Meme', command=lambda: last_meme(memes, meme_seen, image_label) if og == True else last_meme(ai_memes, ai_seen, image_label))
    btn.pack(ipady=10)
    backbtn.pack(ipady=10)

    gene_btn = Button(window, text="Generate Meme", command=lambda: generate_and_show(generate, initial, window))
    gene_btn.pack(ipady=10)

    toggle_og_face = ImageTk.PhotoImage(Image.open("toggle_og.jpg"))
    toggle_ai_face = ImageTk.PhotoImage(Image.open("toggle_ai.jpg"))
    toggle_btn = Button(window, image=toggle_og_face, command=lambda: toggle())
    toggle_btn.pack()

    window.mainloop()
