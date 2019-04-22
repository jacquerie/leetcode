// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
 public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        unordered_set<int> distances = {
            distance(p1, p2),
            distance(p1, p3),
            distance(p1, p4),
            distance(p2, p3),
            distance(p2, p4),
            distance(p3, p4),
        };

        return distances.find(0) == distances.end() && distances.size() == 2;
    }

 private:
    int distance(vector<int>& a, vector<int>& b) {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
    }
};

int main() {
    auto solution = Solution();

    vector<int> p1 = {0, 0}, p2 = {1, 1}, p3 = {1, 0}, p4 = {0, 1};

    assert(solution.validSquare(p1, p2, p3, p4));
}
