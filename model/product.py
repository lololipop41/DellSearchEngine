from data import productDAO


class Product:
    def __init__(self):
        self.product = productDAO

    def view_product(self):
        product_list = self.product.get_product()
        return product_list
