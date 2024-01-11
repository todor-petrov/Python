from product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = [x for x in self.products if x.name == product_name]
        return product[0] if product else None

    def remove(self, product_name):
        product = [x for x in self.products if x.name == product_name]
        self.products.remove(product[0]) if product else None

    def __repr__(self):
        products_info = [f'{p.name}: {p.quantity}' for p in self.products]
        return '\n'.join(products_info)
