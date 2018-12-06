// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <deque>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;

        deque<int> deque;
        for (int i = 0; i < nums.size(); i++) {
            while (!deque.empty() && deque.front() <= i - k) {
                deque.pop_front();
            }

            while (!deque.empty() && nums[i] >= nums[deque.back()]) {
                deque.pop_back();
            }

            deque.push_back(i);

            if (i >= k - 1) {
                result.push_back(nums[deque.front()]);
            }
        }

        return result;
    }
};

int main() {
  auto solution = Solution();

  vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};

  vector<int> expected = {3, 3, 5, 5, 6, 7};
  vector<int> result = solution.maxSlidingWindow(nums, 3);

  assert(expected == result);
}
