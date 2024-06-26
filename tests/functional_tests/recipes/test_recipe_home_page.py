from selenium.webdriver.common.by import By
import pytest
from .base import RecipeBaseFunctionalTest

# Só roda os tests com a mark functional_test:
# pytest -m 'functional_test'

# roda todos os tests menos os com a mark functional_test:
# pytest -m 'not functional_test'


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):

    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here 🥲', body.text)
