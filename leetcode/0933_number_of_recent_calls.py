# -*- coding: utf-8 -*-

from collections import deque


class RecentCounter:
    def __init__(self):
        self.count = 0
        self.queue = deque()

    def ping(self, t):
        while self.queue and t - self.queue[0] > 3000:
            self.count -= 1
            self.queue.popleft()
        self.count += 1
        self.queue.append(t)
        return self.count


if __name__ == "__main__":
    obj = RecentCounter()

    assert 1 == obj.ping(1)
    assert 2 == obj.ping(100)
    assert 3 == obj.ping(3001)
    assert 3 == obj.ping(3002)
