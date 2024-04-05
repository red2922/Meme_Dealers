# April 5th Meme Generator Standup Record #4
&nbsp; At the beginning of this meeting, we discussed the work done so far in this sprint and pushed the completed work
 from this sprint into main. We also figured out why memes were displaying twice when switching from the “Next Meme”
 and “Previous Meme” buttons and vice versa, but decided that this was a low priority for now and will be worked on
 during our bugfix phase. We also continued to discuss the probability of implementing a share button and the options
 presented from research into the topic. We could either use webBrowser, which only opens the linked website (in this
 case, Twitter), but it can’t do anything more. This is much simpler and a much lower security risk, but this means
 that we would have to implement a copy functionality when the user clicks the share button so they can post it manually.
 On the other hand, we could use Selenium, which is much more complex than webBrowser, but this allows us to use the
 user’s sign-in info (if they’re already signed in) and directly paste the meme onto twitter, but this comes with a much
 larger security risk. After much discussion, we decided to implement the webBrowser version for now while doing more
 research into the Selenium version. We then assigned everyone their tasks for the weekend as followed:
- Trey: Standup Record #4 & Testing Documentation
- Isaac: Security Documentation & Share Button
- Mitchell: Share Button
- Jake: Refactoring main into classes instead of functions (this may take multiple sprints)
- Huigwang: Make radio buttons to allow user to change AI meme prompt
