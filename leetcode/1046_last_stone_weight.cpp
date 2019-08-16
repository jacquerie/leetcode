// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

class Solution {
 public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, less<int>> heap;
        for (const auto& stone : stones) {
            heap.push(stone);
        }

        while (heap.size() > 1) {
            int x = heap.top();
            heap.pop();

            int y = heap.top();
            heap.pop();

            if (x > y) {
                heap.push(x - y);
            }
        }

        return heap.size() == 1 ? heap.top() : 0;
    }
};

int main() {
    auto solution = Solution();

    vector<int> stones = {2, 2};

    assert(0 == solution.lastStoneWeight(stones));
}
