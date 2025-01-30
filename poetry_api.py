import random

import requests


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class PoetryDBAPI(metaclass=Singleton):
    BASE_URL = "https://poetrydb.org/"
    RANDOM_POEM_URL = BASE_URL + "random"
    POEM_BY_AUTHOR = BASE_URL + "author/{}"

    def _get_poem(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_random_poem(self):
        return random.choice(self._get_poem(self.RANDOM_POEM_URL))

    def get_poem_by_author(self, author):
        return self._get_poem(self.POEM_BY_AUTHOR.format(author))[0]
