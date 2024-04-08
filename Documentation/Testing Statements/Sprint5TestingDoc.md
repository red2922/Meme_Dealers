# Meme Generator Testing Documentation Sprint 5
## Tested on Mac
- Get Meme and Last Meme work as intended, even when pushing the button multiple times or when there’s nothing to show or flipping between AI and OG memes
-   When switching back and forth, noticed that it also still applies the bug of when swapping from Get Meme to Last Meme that it will transfer over to the other set of memes
-       sentially, the bug is whenever you swap between the buttons you have to click twice to see a different meme, as since the last meme shown and the get meme are the same meme when switching
-       Therefore, when you Get a Meme from OG and then switch to AI (where your last seen was 1.png) and click Last Meme, it will still show the originally gotten AI meme  (1.png) before showing the actual last AI Meme (say, 2.png)
- Generate meme does work as intended; gives me an AI generated meme based on the radio buttons set at the bottom of the page (dog gives me dog meme, cat gives me cat meme, stored appropriately in folder
-   Though anything with the same name gets overwritten, so for instance, the cat.png will always get overwritten when creating another AI cat meme
- The share button takes me to Twitter.com
-   Can’t further test it right now since I don’t have twitter, but looking at the code it looks to be working as intended
- •	Most likely a Mac issue, but clicking buttons without any delay requires me to change the size of the window
