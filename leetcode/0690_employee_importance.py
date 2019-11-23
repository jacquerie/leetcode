# -*- coding: utf-8 -*-

from collections import deque


class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        employees_map = {}
        for employee in employees:
            employees_map[employee.id] = employee

        result = 0

        queue = deque([id])
        while queue:
            employee = employees_map[queue.pop()]
            result += employee.importance
            for subordinate in employee.subordinates:
                queue.append(subordinate)

        return result


if __name__ == '__main__':
    solution = Solution()

    employees = [
        Employee(1, 5, [2, 3]),
        Employee(2, 3, []),
        Employee(3, 3, []),
    ]

    assert 11 == solution.getImportance(employees, 1)
