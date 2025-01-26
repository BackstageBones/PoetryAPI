import requests


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class PoetryDBAPI(metaclass=Singleton):
    BASE_URL = "https://poetrydb.org/"

    def get_random_poem(self):
        url = f"{self.BASE_URL}random"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_poem_by_author(self, author):
        url = f"{self.BASE_URL}author/{author}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
