import allure
import pytest
from assertpy import assert_that


@pytest.mark.usefixtures("request_poetry")
class TestPoetryDB:

    @allure.title("Test random poem form poetry API")
    @allure.description(
        "This test attempts to get random poem from poetry API.\n Fails if any error happens.")
    @allure.tag("Poem", "PoetryAPI", "Sporty")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Adrian Miendlarzewski")
    @allure.link("https://github.com/BackstageBones/PoetryAPI", name="repository")
    @allure.issue("some test issue")
    @allure.testcase("some test case")
    def test_get_random_poem(self):
        poem = self.db.get_random_poem()
        assert_that(poem).contains_key('title')
        assert_that(poem).contains_key('author')
        assert_that(poem).contains_key('lines')
        assert_that(poem).contains_key('linecount')
        assert_that(poem['linecount']).is_digit()

    @allure.title("Test specifics of author's poem")
    @allure.tag("Poem", "PoetryAPI", "Sporty")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Adrian Miendlarzewski")
    @allure.link("https://github.com/BackstageBones/PoetryAPI", name="repository")
    @allure.issue("some test issue")
    @allure.testcase("some test case")
    @pytest.mark.parametrize('author', (["Emily Dickinson", 'Geoffrey Chaucer']))
    def test_get_poem_by_author(self, author: str):
        poem = self.db.get_poem_by_author(author)
        assert_that(poem).contains_key('title')
        assert_that(poem).contains_key('author')
        assert_that(poem['author']).is_equal_to(author)
        assert_that(poem).contains_key('lines')
        assert_that(poem['title']).is_not_empty()
        assert_that(poem['lines']).is_not_empty()
        assert_that(poem['lines']).is_instance_of(list)
