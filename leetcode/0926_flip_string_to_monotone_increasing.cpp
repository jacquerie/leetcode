// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int minFlipsMonoIncr(string S) {
        int ones_count = 0, result = 0;

        for (const auto& c : S) {
            if (c == '0' && ones_count == 0) {
                continue;
            } else if (c == '0') {
                result++;
            } else {
                ones_count++;
            }

            result = min(result, ones_count);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.minFlipsMonoIncr("00110"));
    assert(2 == solution.minFlipsMonoIncr("010110"));
    assert(2 == solution.minFlipsMonoIncr("00011000"));
    assert(3 == solution.minFlipsMonoIncr("0101100011"));
}
