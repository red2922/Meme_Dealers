from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import base64

# Note this code will not work if there is no .env file present + API Key
env = load_dotenv(find_dotenv())
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")


class ImageGenerate:
    def __init__(self, prompt: str):
        self._prompt = prompt
        self._model = "dall-e-3"
        self._size = "1024x1024"
        self._quality = "standard"
        self._number = 1
        self._image = None

    def get_prompt(self):
        return self._prompt

    def set_prompt(self, new: str):
        self._prompt = new

    def get_model(self):
        return self._model

    def set_model(self, new: str):
        self._model = new

    def get_size(self):
        return self._size

    def set_size(self, new: str):
        self._size = new

    def get_quality(self):
        return self._quality

    def set_quality(self, new: str):
        self._quality = new

    def get_number(self):
        return self._number

    def set_number(self, new: int):
        self._number = new

    def get_data(self):
        return self._image
    
    def set_data(self, new):
        self._image = new

    def get_url(self):
        return self.get_data().data[0].url


    def generateImage(self):
        image = client.images.generate(model=self.get_model(),
                                       prompt=self.get_prompt(),
                                       size=self.get_size(),
                                       quality=self.get_quality(),
                                       n=1,
                                        response_format="b64_json" )

        self.set_data(image)
        #return image.data[0].url
    
    def saveImage(self, name:str):
        new = open(name, "wb")
        new.write(base64.b64decode(self.get_data().data[0].b64_json))
        new.close()


# How to use the generator
#Generator = ImageGenerate("Make me a meme of a dog")
#Generator.generateImage()
#Generator.saveImage("Code\AI_Memes\Dog.png")
