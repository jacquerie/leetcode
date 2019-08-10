// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    string defangIPaddr(string address) {
        string result;

        for (const auto& c : address) {
            if (c == '.') {
                result.append("[.]");
            } else {
                result.push_back(c);
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert("1[.]1[.]1[.]1" == solution.defangIPaddr("1.1.1.1"));
    assert("255[.]100[.]50[.]0" == solution.defangIPaddr("255.100.50.0"));
}
