# -*- coding: utf-8 -*-


class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0
        return self.prefix_products[-1] // self.prefix_products[-(k + 1)]


if __name__ == "__main__":
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    assert 20 == obj.getProduct(2)
    assert 40 == obj.getProduct(3)
    assert 0 == obj.getProduct(4)
    obj.add(8)
    assert 32 == obj.getProduct(2)
