# -*- coding: utf-8 -*-


class Solution:
    def findRestaurant(self, list1, list2):
        dict1 = {name: i for i, name in enumerate(list1)}
        dict2 = {name: i for i, name in enumerate(list2)}

        min_index_sum, result = float("inf"), {}

        for name in dict1:
            if name in dict2:
                result[name] = dict1[name] + dict2[name]
                min_index_sum = min(min_index_sum, result[name])

        return [
            name for name, index_sum in result.items() if index_sum == min_index_sum
        ]


if __name__ == "__main__":
    solution = Solution()

    assert ["Shogun"] == solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
    )
    assert ["Shogun"] == solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"],
    )
