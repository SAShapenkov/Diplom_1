import random

from praktikum.ingredient import Ingredient
from unittest.mock import Mock


class TestIngredientsMocked:
    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [
        Ingredient('INGREDIENT_TYPE_SAUCE', 'red_hot_chili_sauce', 500),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'mayonae ketchup', 770),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'matall sauce', 2),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'yellow asteroid sauce', 14),
        Ingredient('INGREDIENT_TYPE_FILLING', 'pineaple meat', 100),
        Ingredient('INGREDIENT_TYPE_FILLING', 'shark noses', 350)
    ]
    def test_ingredient_name(self):
        ingredient = random.choice(self.mock_available_ingredients())
        name = ingredient.name
        factual_name = ingredient.get_name()
        assert name == factual_name

    def test_ingredient_price(self):
        ingredient = random.choice(self.mock_available_ingredients())
        price = ingredient.price
        factual_price = ingredient.get_price()
        assert price == factual_price

    def test_ingredient_type(self):
        ingredient = random.choice(self.mock_available_ingredients())
        ingredient_type = ingredient.type
        factual_type = ingredient.get_type()
        assert ingredient_type == factual_type