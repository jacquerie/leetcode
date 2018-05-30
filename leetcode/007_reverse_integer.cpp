#include <cassert>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int previous, result = 0;

        while (x) {
            previous = result;

            result *= 10;
            result += x % 10;
            if (result / 10 != previous) {
                return 0;
            }

            x /= 10;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(321 == solution.reverse(123));
    assert(-321 == solution.reverse(-123));
    assert(21 == solution.reverse(120));
}
