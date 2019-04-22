// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    string convertToTitle(int n) {
        string result;

        while (n) {
            result.insert(0, 1, 'A' + (n - 1) % 26);
            n = (n - 1) / 26;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert("A" == solution.convertToTitle(1));
    assert("AB" == solution.convertToTitle(28));
    assert("ZY" == solution.convertToTitle(701));
}
