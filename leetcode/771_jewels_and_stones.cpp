#include <cassert>
#include <string>

using namespace std;

class Solution {
public:
    int numJewelsInStones (string J, string S) {
        int result = 0;

        for (auto c: S) {
            if (J.find(c) != string::npos) {
                result++;
            }
        }

        return result;
    }
};

int main () {
    auto solution = Solution();

    assert(3 == solution.numJewelsInStones("aA", "aAAbbbb"));
    assert(0 == solution.numJewelsInStones("z", "ZZ"));
}
