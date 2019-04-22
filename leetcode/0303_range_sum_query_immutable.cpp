// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class NumArray {
 public:
    explicit NumArray(vector<int> nums) {
        sums_.push_back(0);
        for (auto num : nums) {
            sums_.push_back(sums_.back() + num);
        }
    }

    int sumRange(int i, int j) {
        return sums_[j + 1] - sums_[i];
    }

 private:
    vector<int> sums_;
};

int main() {
    vector<int> nums = {-2, 0, 3, -5, 2, -1};

    auto obj = NumArray(nums);

    assert(1 == obj.sumRange(0, 2));
    assert(-1 == obj.sumRange(2, 5));
    assert(-3 == obj.sumRange(0, 5));
}
