import sys
from pathlib import Path

# mypy: disable-error-code="import-untyped"
from models import Category, Product

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_add_product():
    cat = Category("Test", "desc", [])
    prod = Product("name", "desc", 1000, 2)
    cat.add_product(prod)
    assert "name" in cat.products
    assert cat.product_count == 1


def test_price_setter_positive(monkeypatch):
    prod = Product("Test", "desc", 1000, 1)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    prod.price = 800
    assert prod.price == 800


def test_price_setter_negative(capfd):
    prod = Product("Test", "desc", 1000, 1)
    prod.price = -500
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert prod.price == 1000


def test_new_product():
    data = {"name": "X", "description": "desc", "price": 100, "quantity": 5}
    prod = Product.new_product(data)
    assert isinstance(prod, Product)
    assert prod.name == "X"
