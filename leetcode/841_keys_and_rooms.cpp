// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <queue>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
 public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        unordered_set<int> visited = {0};

        queue<int> queue;
        queue.push(0);

        while (!queue.empty()) {
            auto i = queue.front();
            queue.pop();

            for (auto j : rooms[i]) {
                if (visited.find(j) == visited.end()) {
                    visited.insert(j);
                    queue.push(j);
                }
            }
        }

        return visited.size() == rooms.size();
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> rooms = {{1}, {2}, {3}, {}};

    assert(solution.canVisitAllRooms(rooms));
}
