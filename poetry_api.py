import random

import requests

from poetry_endpoints import PoetryEndpoints


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class PoetryDBAPI(metaclass=Singleton):

    def __init__(self):
        self.session = requests.Session()

    def _get_poem(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_random_poem(self):
        return random.choice(self._get_poem(PoetryEndpoints.RANDOM_POEM_URL.value))

    def get_poem_by_author(self, author):
        return self._get_poem(PoetryEndpoints.POEM_BY_AUTHOR.value.format(author))[0]
