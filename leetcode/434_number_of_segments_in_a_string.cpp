#include <cassert>
#include <cctype>
#include <string>

using namespace std;

class Solution {
public:
    int countSegments (string s) {
        if (s.empty()) {
            return 0;
        }

        bool inWord = !(isspace(s[0]));
        int result = 0;

        for (auto c : s) {
            if (isspace(c) && inWord) {
                inWord = false;
                result++;
            } else if (!isspace(c)) {
                inWord = true;
            }
        }

        if (inWord) {
            result++;
        }

        return result;
    }
};

int main () {
    auto solution = Solution();

    assert(5 == solution.countSegments("Hello, my name is John"));
    assert(5 == solution.countSegments(" Hello, my name is John"));
    assert(5 == solution.countSegments("Hello, my name is John "));
    assert(5 == solution.countSegments("Hello, my  name is John"));
    assert(0 == solution.countSegments(""));
}
