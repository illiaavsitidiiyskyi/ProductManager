from models import Product

# отримання
def get_all_products():
    return Product.select()


def get_product_by_category(category: str):
    return Product.select().where(Product.category == category)


def get_all_categories():
    return Product.select(Product.category).distinct().order_by(Product.category)


def product_exist(name) -> bool:
    return Product.select().where(Product.name == name).exists()

# додавання
def add_product(name: str, price: float, category: str ):
    Product.create(name=name, price=price, category=category)
# видалення