# Sprint 4 Security Statement
AI implementation means that prompts and API keys must be watched.  In order to keep the DALL-E API key secure, it is currently stored within a .env file on each user's computer, separate from the rest of the project.
This is to prevent the API key from being leaked and abused by anyone outside of the project.  Without this measure, the API key could potentially be leaked and allow for unmonitered and illigitemate uses of the
AI.  Due to a small cost being attached to each generation of an AI meme, this unmonitered use would be a problem as it could quickly cause a large cost to build up.
The prompt is currently only changable within the code itself to prevent issues with DALL-E as DALL-E does not allow prompts it consideres inappropriate, which can lead to a ban on the API key being used.  To prevent this 
issue, user input will be severely limited to keep the user from causing issues within the program.  This planning will be further expanded upon in future sprints.
