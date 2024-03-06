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
    def test_ingredient(self):
        ingredient = random.choice(self.mock_available_ingredients())
        name = ingredient.name
        price = ingredient.price
        ingredient_type = ingredient.type
        factual_name = ingredient.get_name()
        factual_price = ingredient.get_price()
        factual_type = ingredient.get_type()
        assert name == factual_name and price == factual_price and ingredient_type == factual_type