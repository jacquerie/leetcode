// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int peakIndexInMountainArray(vector<int>& A) {
        int mid, first = 0, last = A.size() - 1;

        while (first <= last) {
            mid = (first + last) / 2;
            if (A[mid] < A[mid + 1]) {
                first = mid + 1;
            } else {
                last = mid - 1;
            }
        }

        return first;
    }
};

int main() {
    auto solution = Solution();

    vector<int> A = {0, 1, 0};

    assert(1 == solution.peakIndexInMountainArray(A));
}
