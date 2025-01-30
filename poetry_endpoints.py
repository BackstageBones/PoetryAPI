from enum import Enum


class PoetryEndpoints(Enum):
    BASE_URL = "https://poetrydb.org/"
    RANDOM_POEM_URL = "https://poetrydb.org/random"
    POEM_BY_AUTHOR = "https://poetrydb.org/author/{}"