#include <cassert>

using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        while (b) {
            int carry = a & b;
            a ^= b;
            b = carry << 1;
        }

        return a;
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.getSum(1, 2));
}
