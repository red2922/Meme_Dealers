# Meme Generator Sprint 6 Mac Testing Documentation
- Switching between OG & AI still works as expected, even when mixing get memes and last memes between switching
  - Pressing get meme after switching source pulls from correct source and treats each source as usual (If the previous time on said list was Last Meme and then you choose get meme, it will show the original meme last seen and then a new meme, and vice versa)
- Generate Meme works as usual, even with new prompt
  - Though newly made meme is not added to current source until program is reran
- Share buttons work as expected, but forces me to go into fullscreen mode in order to click them
  - This is fine, but causes an issue of how on Mac the response time is horrid unless I change window size manually and then go into it. Maybe allow user to scroll?
- Images are scaled correctly
