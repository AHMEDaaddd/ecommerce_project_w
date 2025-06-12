"""Модуль содержит Product и Category для работы с товарами и категориями."""


class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует товар с именем, описанием, ценой и количеством."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену с валидацией и подтверждением понижения."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            choice = (
                input("Цена понижается. Подтвердите действие (y/n):" " ")
                .strip()
                .lower()
            )
            if choice == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Создает новый экземпляр товара из словаря данных."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )


class Category:
    """Класс для представления категории товаров."""

    product_counter = 0
    """Класс для представления категории товаров."""

    def __init__(self, name: str, description: str, products: list["Product"]):
        """Класс для представления категории товаров."""
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Создает категорию с названием, описанием и списком товаров."""
        self.__products.append(product)
        Category.product_counter += 1

    @property
    def products(self) -> str:
        """Добавляет товар в категорию и увеличивает счетчик товаров."""
        return "".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
            for p in self.__products
        )

    @property
    def product_count(self) -> int:
        """Возвращает строку со списком всех товаров в категории."""
        return len(self.__products)
