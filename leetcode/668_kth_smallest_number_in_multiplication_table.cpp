// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
 public:
    int findKthNumber(int m, int n, int k) {
        int mid, first = 1, last = m * n;

        while (first <= last) {
            mid = (first + last) / 2;
            if (countSmaller(m, n, mid) >= k) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return first;
    }

 private:
    int countSmaller(int m, int n, int target) {
        int result = 0;
        for (int i = 1; i <= m; i++) {
            result += min(target / i, n);
        }
        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.findKthNumber(3, 3, 5));
    assert(6 == solution.findKthNumber(2, 3, 6));
}
