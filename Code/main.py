from tkinter import *
from PIL import ImageTk, Image
import random
import os
from io import BytesIO
import win32clipboard
from open_api import ImageGenerate
import webbrowser

def load_memes(dir):
    memeList = []
    for meme in os.listdir(dir):
        filePath = dir + meme # Directory attached to filename for easy getting
        memeList.append(filePath)
    random.shuffle(memeList)
    return memeList


def resize_img(img, height):
    height_rate = height / float(img.size[1])
    width = int(float(img.size[0]) * float(height_rate))
    return img.resize((width, height))


def get_random_meme(memeList, meme_ind, check, label, user_inp):
    check[0] = 0
    meme = memeList[meme_ind[0]]
    meme_ind[0] += 1
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img, 500))
    label.config(image=meme_resized)
    label.image = meme_resized  # Keep a reference to the image object
    print(str(meme))
    if len(user_inp) == 8:
        user_inp.pop(0)
    user_inp.append("get")
    return meme


def last_meme(memeList, meme_ind, check, label, user_inp, konami_code):
    check[0] = 1
    meme_ind[0] -= 1
    if meme_ind[0] < 0:
        meme_ind[0] = 0
    meme = memeList[meme_ind[0]]
    meme_img = Image.open(meme)
    meme_resized = ImageTk.PhotoImage(resize_img(meme_img, 500))
    label.config(image=meme_resized)
    label.image = meme_resized
    if len(user_inp) == 8:
        user_inp.pop(0)
    user_inp.append("last")
    if user_inp == konami_code:
        webbrowser.open("https://www.youtube.com/watch?v=3VBn4b1rxf0")
    return meme


def toggle():
    global og
    if og:
        toggle_btn.config(image=toggle_ai_face)
        og = False
    else:
        toggle_btn.config(image=toggle_og_face)
        og = True


def copyToClipboard(meme):
    memeImg = Image.open(meme)
    output = BytesIO()
    memeImg.convert('RGB').save(output, "BMP")
    byteMeme = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, byteMeme)
    win32clipboard.CloseClipboard()
    print("Clipboard")


def share(check, website):
    webbrowser.open(website)

    if check[0] == 0 and og == True:
        meme = last_meme(memes, meme_ind, check, image_label, user_inp=[], konami_code=0)
    elif check[0] == 1 and og == True:
        meme = get_random_meme(memes, meme_ind, check, image_label, user_inp=[])
    elif check[0] == 0 and og == False:
        meme = last_meme(ai_memes, ai_ind, check, image_label, user_inp=[], konami_code=0)
    else:
        meme = get_random_meme(ai_memes, ai_ind, check, image_label, user_inp=[])
    print(meme)
    copyToClipboard(meme)
    print("The code got to here")


def set_file_name(prompt):
    return prompt.split()[6] + str(random.randint(0,100000000)) + ".png"

def generate_and_show(connect: ImageGenerate, prompt: str, window: Tk):
    connect.set_prompt(prompt)
    file_name = set_file_name(prompt)
    direct = "AI_Memes/" + file_name

    new = Toplevel(window)
    new.title(file_name)
    new.geometry("1352x878")

    connect.generateImage()
    connect.saveImage(direct)
    
    new_Image = Image.open(direct)
    ai_image = ImageTk.PhotoImage(resize_img(new_Image, 500))
    Label(new, image=ai_image).pack()
    new.mainloop()


def prompt_rad():
    global initial
    if prompt.get() == 0:
        initial = 'Make me a meme of a dog'
    elif prompt.get() == 1:
        initial = 'Make me a meme of a cat'
    elif prompt.get() == 2:
        initial = 'Make me a meme of a programmer'


def adjective_rad(initial):
    if adjective.get() == 0:
        initial += ' that is an alpha'
    elif adjective.get() == 1:
        initial += ' that is a beta'
    elif adjective.get() == 2:
        initial += ' that is a sigma'
    elif adjective.get() == 3:
        initial += ' that is a giga'


if __name__ == "__main__":
    global og

    meme_dir = 'Memes for Meme God/'
    ai_dir = 'AI_Memes/'
    initial = "Make me a meme of a dog"
    meme_ind = [0]
    ai_ind = [0]
    back_forward_check = [0]
    og = True
    konami_code = ["get", "get", "last", "last", "get", "last", "get", "last"]
    user_inp = []

    generate = ImageGenerate(initial)

    window = Tk()
    window.title('Meme Dealers')
    window.geometry('1512x982+0+0')

    welcome_img = Image.open('Welcome.jpg')
    welcome = ImageTk.PhotoImage(resize_img(welcome_img, 500))
    image_label = Label(window, image=welcome)
    image_label.pack(pady=(10, 10))

    toggle_og_face = ImageTk.PhotoImage(Image.open("toggle_og.jpg"))
    toggle_ai_face = ImageTk.PhotoImage(Image.open("toggle_ai.jpg"))
    toggle_btn = Button(window, image=toggle_og_face, command=lambda: toggle())
    toggle_btn.place(x=20, y=250)

    memes = load_memes(meme_dir)
    ai_memes = load_memes(ai_dir)

    btn_frame = Frame(window)
    btn_frame.pack()

    btn = Button(btn_frame, text='Get Meme', command=lambda: get_random_meme(memes, meme_ind, back_forward_check, image_label, user_inp) if og == True else get_random_meme(ai_memes, ai_ind, back_forward_check, image_label, user_inp))
    back_btn = Button(btn_frame, text='Last Meme', command=lambda: last_meme(memes, meme_ind, back_forward_check, image_label, user_inp,konami_code) if og == True else last_meme(ai_memes, ai_ind, back_forward_check, image_label, user_inp, konami_code))
    btn.pack(side='right', ipady=10)
    back_btn.pack(side='left', ipady=10)

    gene_btn = Button(window, text="Generate Meme", command=lambda: generate_and_show(generate, initial, window))
    gene_btn.pack(ipady=10)

    prompt = IntVar()

    prompt_dog = Radiobutton(window, text='Dog', variable=prompt, value=0, command=lambda: prompt_rad())
    prompt_cat = Radiobutton(window, text='Cat', variable=prompt, value=1, command=lambda: prompt_rad())
    prompt_programmer = Radiobutton(window, text='Programmer', variable=prompt, value=2, command=lambda: prompt_rad())
    prompt_dog.pack()
    prompt_cat.pack()
    prompt_programmer.pack()

    adjective = IntVar()

    adj_alpha = Radiobutton(window, text='Alpha', variable=adjective, value=0, command=lambda: adjective_rad())
    adj_beta = Radiobutton(window, text='Beta', variable=adjective, value=1, command=lambda: adjective_rad())
    adj_sigma = Radiobutton(window, text='Sigma', variable=adjective, value=2, command=lambda: adjective_rad())
    adj_giga = Radiobutton(window, text='Giga', variable=adjective, value=3, command=lambda: adjective_rad())
    adj_alpha.pack()
    adj_beta.pack()
    adj_sigma.pack()
    adj_giga.pack()

    share_btn_frame = Frame(window)
    share_btn_frame.pack(pady=(50, 10))

    share_label = Label(window, text="Share", font=("TkDefaultFont", 20))
    discord_img = ImageTk.PhotoImage(resize_img(Image.open('discord.png'), 64))
    facebook_img = ImageTk.PhotoImage(resize_img(Image.open('facebook.png'),64))
    reddit_img = ImageTk.PhotoImage(resize_img(Image.open('Reddit.png'), 64))
    twitter_img = ImageTk.PhotoImage(resize_img(Image.open('twitter.jpg'),64))
    bad_img = ImageTk.PhotoImage(resize_img(Image.open('bad.png'), 64))
    share_twitter = Button(window, image=twitter_img, command=lambda: share(back_forward_check, 'https://twitter.com/home'))
    share_discord = Button(window, image=discord_img, command=lambda: share(back_forward_check, 'https://discord.com/channels/@me'))
    share_reddit = Button(window, image=reddit_img, command=lambda: share(back_forward_check, 'https://www.reddit.com/'))
    share_facebook = Button(window, image=facebook_img, command=lambda: share(back_forward_check, 'https://www.facebook.com/'))
    happy_easter = Button(window, image=bad_img, command=lambda: share(back_forward_check, 'https://www.oxfordlearnersdictionaries.com/definition/american_english/awful_1'))
    share_label.place(x=50, y=310)
    share_twitter.place(x=50, y=650)
    share_discord.place(x=50, y=575)
    share_facebook.place(x=50, y=500)
    share_reddit.place(x=50, y=425)
    happy_easter.place(x=50, y=350)

    window.mainloop()

