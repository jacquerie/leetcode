#include <cassert>

using namespace std;

int guess (int num) {
    if (num > 6) {
        return -1;
    } else if (num == 6) {
        return 0;
    } else if (num < 6) {
        return 1;
    }
}

class Solution {
public:
    int guessNumber (int n) {
        int mid, first = 1, last = n;

        while (first <= last) {
            mid = first + (last - first) / 2;
            if (guess(mid) <= 0) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return first;
    }
};

int main () {
    auto solution = Solution();

    assert(6 == solution.guessNumber(10));
}
