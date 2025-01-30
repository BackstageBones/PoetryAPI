import pytest

from poetry_api import PoetryDBAPI


@pytest.fixture(scope='class')
def request_poetry(request):
    client = PoetryDBAPI()
    request.cls.db = client
    yield client
    del request.cls.db
    del client