// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstdlib>
#include <vector>

using namespace std;

class Solution {
 public:
    explicit Solution(vector<int> nums): nums_(nums), seed_(0) {}

    int pick(int target) {
        int count = 0, reservoir;

        for (int i = 0; i < nums_.size(); i++) {
            if (nums_[i] == target) {
                if (rand_r(&seed_) % ++count == 0) {
                    reservoir = i;
                }
            }
        }

        return reservoir;
    }

 private:
    const vector<int> nums_;
    unsigned int seed_;
};

int main() {
    vector<int> nums = {1, 2, 3, 3, 3};

    auto solution = Solution(nums);

    assert(2 == solution.pick(3));
    assert(0 == solution.pick(1));
}
