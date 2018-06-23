// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>

using namespace std;

bool isBadVersion(int version) {
    return version >= 3;
}

class Solution {
 public:
    int firstBadVersion(int n) {
        int mid, first = 1, last = n;

        while (first <= last) {
            mid = first + (last - first) / 2;
            if (isBadVersion(mid)) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return first;
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.firstBadVersion(5));
}
