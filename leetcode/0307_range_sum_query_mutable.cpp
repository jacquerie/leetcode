// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class FenwickTree {
 public:
    explicit FenwickTree(vector<int> nums): els_(nums.size() + 2, 0) {
        for (int i = 0; i < nums.size(); i++) {
            add(i + 1, nums[i]);
        }
    }

    void add(int i, int k) {
        while (i < els_.size()) {
            els_[i] += k;
            i += i & -i;
        }
    }

    int sumPrefix(int i) {
        int result = 0;
        while (i > 0) {
            result += els_[i];
            i -= i & - i;
        }
        return result;
    }

 private:
    vector<int> els_;
};

class NumArray {
 public:
    explicit NumArray(vector<int> nums): tree_(nums) {}

    void update(int i, int val) {
        tree_.add(i + 1, val - sumRange(i, i));
    }

    int sumRange(int i, int j) {
        return tree_.sumPrefix(j + 1) - tree_.sumPrefix(i);
    }

 private:
    FenwickTree tree_;
};

int main() {
  vector<int> nums = {1, 3, 5};

  auto obj = NumArray(nums);

  assert(9 == obj.sumRange(0, 2));
  obj.update(1, 2);
  assert(8 == obj.sumRange(0, 2));
}
