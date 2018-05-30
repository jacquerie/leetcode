#include <cassert>

class Solution {
public:
    int climbStairs(int n) {
        int previous = 1, current = 1;

        for (int i = 1; i < n; i++) {
            int tmp = current;
            current += previous;
            previous = tmp;
        }

        return current;
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.climbStairs(1));
    assert(2 == solution.climbStairs(2));
    assert(3 == solution.climbStairs(3));
    assert(5 == solution.climbStairs(4));
    assert(8 == solution.climbStairs(5));
}
