#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int minI = m, minJ = n;

        for (auto op : ops) {
            if (op[0] < minI) {
                minI = op[0];
            }

            if (op[1] < minJ) {
                minJ = op[1];
            }
        }

        return minI * minJ;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> ops = {{2, 2}, {3, 3}};

    int expected = 4;
    int result = solution.maxCount(3, 3, ops);

    assert(expected == result);
}
