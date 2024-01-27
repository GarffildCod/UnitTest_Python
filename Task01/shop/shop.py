class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sort_products_by_price(self):
        self.products.sort(key=lambda x: x.price)

    def get_most_expensive_product(self):
        if not self.products:
            return None
        return max(self.products, key=lambda x: x.price)