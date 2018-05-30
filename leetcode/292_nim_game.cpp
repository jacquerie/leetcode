#include <cassert>

using namespace std;

class Solution {
public:
    bool canWinNim(int n) {
        return n % 4 != 0;
    }
};

int main() {
    auto solution = Solution();

    assert(!solution.canWin(4));
}
