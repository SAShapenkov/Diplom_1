from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import pytest


def test_get_receipt():
    bun_name = 'simple_bun'
    bun = Bun(name=bun_name, price=1.1)
    ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', 'red_hot_chili_sauce', 0.0)
    ingredient2 = Ingredient('INGREDIENT_TYPE_FILLING', 'pineaple meat', 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    receipt = burger.get_receipt()
    assert '(==== simple_bun ====)' in receipt and '= ingredient_type_sauce red_hot_chili_sauce =' in receipt and'= ingredient_type_filling pineaple meat =' in receipt


def test_burger_buns_only():
    bun = Bun(name='simple_bun', price=1.1)
    burger = Burger()
    burger.set_buns(bun)
    receipt = burger.get_receipt()
    assert bun.get_name() in receipt


def test_burger_buns_and_sause():
    bun_name = 'simple_bun'
    bun = Bun(name=bun_name, price=1.1)
    ingredient = Ingredient('INGREDIENT_TYPE_SAUCE', 'red_hot_chili_sauce', 0.0)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert ingredient.get_name() in receipt and ingredient.get_type().lower() in receipt


def test_burger_buns_and_fillings():
    bun_name = 'simple_bun'
    bun = Bun(name=bun_name, price=1.1)
    ingredient = Ingredient('INGREDIENT_TYPE_FILLING', 'pineaple meat', 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert ingredient.get_name() in receipt and ingredient.get_type().lower() in receipt


def test_burger_ingredients_can_be_removed():
    bun_name = 'simple_bun'
    bun = Bun(name=bun_name, price=1.1)
    ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', 'red_hot_chili_sauce', 0.0)
    ingredient2 = Ingredient('INGREDIENT_TYPE_FILLING', 'pineaple meat', 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.remove_ingredient(0)
    receipt = burger.get_receipt()
    assert ingredient1.get_name() not in receipt and ingredient2.get_name() in receipt


def test_burger_ingredients_positions_can_be_replaced():
    bun_name = 'simple_bun'
    bun = Bun(name=bun_name, price=1.1)
    ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', 'red_hot_chili_sauce', 0.0)
    ingredient2 = Ingredient('INGREDIENT_TYPE_FILLING', 'pineaple meat', 100)
    name1 = ingredient1.get_name()
    name2 = ingredient2.get_name()
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    receipt = burger.get_receipt()
    index1 = receipt.find(name1)
    index2 = receipt.find(name2)
    burger.move_ingredient(0, 1)
    receipt_new = burger.get_receipt()
    new_index1 = receipt_new.find(name1)
    new_index2 = receipt_new.find(name2)
    assert index1 < index2 and new_index1 > new_index2


@pytest.mark.parametrize('name, price', [
    ['saturn bun', 0.0],
    ['arrakis sand cloud', 5],
    ['cyberbunk', 4],
    ['antimatter special bun', 2]
])
def test_burger_buns_total_price(name, price):
    bun = Bun(name, price)
    burger = Burger()
    burger.set_buns(bun)
    expected_price = bun.get_price() * 2
    actual_price = burger.get_price()
    assert expected_price == actual_price


@pytest.mark.parametrize('name, price', [
    ['saturn bun', 0.0],
    ['arrakis sand cloud', 5],
    ['cyberbunk', 4],
    ['antimatter special bun', 2]
])
def test_burger_buns_multiple_ingredient_total_price(name, price):
    ingredients_list = [
        ['INGREDIENT_TYPE_SAUCE', 'red_hot_chili_sauce', 0.0],
        ['INGREDIENT_TYPE_SAUCE', 'mayonae ketchup', 10],
        ['INGREDIENT_TYPE_SAUCE', 'matall sauce', 15],
        ['INGREDIENT_TYPE_SAUCE', 'some one that you used to know', 0],
        ['INGREDIENT_TYPE_FILLING', 'pineaple meat', 100],
        ['INGREDIENT_TYPE_FILLING', 'shark noses', 350]]
    bun = Bun(name, price)
    burger = Burger()
    burger.set_buns(bun)
    order_price = bun.get_price() * 2
    for elem in ingredients_list:
        ingredient = Ingredient(ingredient_type=elem[0],
                                name=elem[1], price=elem[2])
        burger.add_ingredient(ingredient)
        order_price += ingredient.get_price()

    actual_price = burger.get_price()
    assert order_price == actual_price
