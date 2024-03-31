from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

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

    def generateImage(self):
        image = client.images.generate(model=self.get_model(),
                                       prompt=self.get_prompt(),
                                       size=self.get_size(),
                                       quality=self.get_quality(),
                                       n=1, )

        return image.data[0].url

# How to use the generator
# ImageGenerate("Make me a meme of a cat hanging in there")
# print(Generator.generateImage())
