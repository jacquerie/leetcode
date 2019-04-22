// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int numTrees(int n) {
        vector<int> result = {1};

        for (int i = 0; i < n; i++) {
            int partial = 0;
            for (int j = 0; j < i + 1; j++) {
                partial += result[j] * result[i - j];
            }
            result.push_back(partial);
        }

        return result.back();
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.numTrees(1));
    assert(2 == solution.numTrees(2));
    assert(5 == solution.numTrees(3));
}
