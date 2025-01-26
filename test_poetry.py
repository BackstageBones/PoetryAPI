import pytest
from assertpy import assert_that


@pytest.mark.usefixtures("request_poetry")
class TestPoetryDB:

    def test_get_random_poem(self):
        poem = self.db.get_random_poem()[0]
        assert_that(poem).contains_key('title')
        assert_that(poem).contains_key('author')
        assert_that(poem).contains_key('lines')

    def test_get_poem_by_author(self):
        author = "Emily Dickinson"
        poem = self.db.get_poem_by_author(author)[0]
        assert_that(poem).contains_key('title')
        assert_that(poem).contains_key('author')
        assert_that(poem['author']).is_equal_to(author)
        assert_that(poem).contains_key('lines')
        assert_that(poem['title']).is_not_empty()
        assert_that(poem['lines']).is_not_empty()
        assert_that(poem['lines']).is_instance_of(list)
