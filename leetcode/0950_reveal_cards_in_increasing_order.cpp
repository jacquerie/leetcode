// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <deque>
#include <functional>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> deckRevealedIncreasing(vector<int>& deck) {
    sort(deck.begin(), deck.end(), greater<int>());

    deque<int> queue;
    for (const auto& card : deck) {
      if (!queue.empty()) {
        auto back = queue.back();
        queue.pop_back();
        queue.push_front(back);
      }

      queue.push_front(card);
    }

    return vector<int>(queue.begin(), queue.end());
  }
};

int main() {
  auto solution = Solution();

  vector<int> nums = {17, 13, 11, 2, 3, 5, 7};

  vector<int> expected = {2, 13, 3, 11, 5, 17, 7};
  vector<int> result = solution.deckRevealedIncreasing(nums);

  assert(expected == result);
}
