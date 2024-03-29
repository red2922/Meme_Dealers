import streamlit as st
import random
import os

#hello

# NOTE: To run this you need to get into your python terminal and run the command:
# streamlit run "filename.py"
# At least, my Pycharm required me to do this


def loadmemes():
    direc = 'Memes for Meme God/'
    memeList = []
    for meme in os.listdir(direc):
        filePath = direc + meme # Directory attached to filename for easy getting
        memeList.append(filePath)
    return memeList


def getmeme(memeList):
    meme = memeList[random.randint(0, len(memeList) - 1)]
    st.subheader('Your meme, your magesty')
    st.image(meme)




def main():
    memeList = loadmemes()
    st.button('Get Meme', type="primary")
    if st.button:
        getmeme(memeList)


if __name__ == "__main__":
    main()
