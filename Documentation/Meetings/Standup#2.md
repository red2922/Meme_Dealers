# April 1st Meme Generator Standup #2
&nbsp; This standup meeting started off with running the current program iteration and discussing problems faced during and 
after development. We were able to convert the previous iteration from streamlit to TkInter, and we established an API 
in order to communicate with OpenAI to generate new memes. Through this testing and discussion, the major bug that we 
found was the scaling of images, as some images were so large that they would prevent the user from loading another meme 
and could only close the program. We also discovered that Macs specifically took longer to allow the user to click the 
generate meme button in order to get a new meme. With these bugs addressed, we then moved onto features that could be 
added to the program. These features included using the Stack Algorithm to better handle the loading and saving of images, 
a toggle button to choose whether the user wants an AI-generated meme or a Locally Stored Meme, a download button to 
download the currently displayed meme, a share button to share a meme with another person, a Forward & Backward Button to 
allow the user to look through the currently generated memes, the continuation of working with the API and connecting with 
DALLE and ChatGPT in order to create new memes, and a better UI design. After this discussion, we assigned each member with 
their tasks:
•	Mitchell would work on a Mockup UI and the Toggle Button
•	Trey would work on the documentation and the Download Button
•	Jake would work on the API
•	Isaac would work on the Security side and implementation of the Stack Algorithm and Backward/Forward Buttons
•	Huigwang would work on fixing Image Size display and setting the default window sizes
