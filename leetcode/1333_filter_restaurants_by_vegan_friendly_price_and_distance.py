# -*- coding: utf-8 -*-

from typing import List


class Restaurant:
    def __init__(self, id, rating, veganFriendly, price, distance):
        self.id = id
        self.rating = rating
        self.veganFriendly = veganFriendly
        self.price = price
        self.distance = distance


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        return [
            restaurant.id
            for restaurant in sorted(
                (
                    restaurant
                    for restaurant in (Restaurant(*args) for args in restaurants)
                    if (
                        (restaurant.veganFriendly == 1 if veganFriendly == 1 else True) and
                        restaurant.price <= maxPrice and
                        restaurant.distance <= maxDistance
                    )
                ),
                key=lambda restaurant: (-restaurant.rating, -restaurant.id)
            )
        ]


if __name__ == '__main__':
    solution = Solution()

    assert [3, 1, 5] == solution.filterRestaurants([[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], 1, 50, 10)
    assert [4, 3, 2, 1, 5] == solution.filterRestaurants([[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], 0, 50, 10)
    assert [4, 5] == solution.filterRestaurants([[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], 0, 30, 3)
