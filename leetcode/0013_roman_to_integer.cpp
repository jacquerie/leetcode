// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
 public:
    int romanToInt(string s) {
        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && roman_to_numeral_map_[s[i]] > roman_to_numeral_map_[s[i - 1]]) {
                result += roman_to_numeral_map_[s[i]] - 2 * roman_to_numeral_map_[s[i - 1]];
            } else {
                result += roman_to_numeral_map_[s[i]];
            }
        }

        return result;
    }

 private:
    unordered_map<char, int> roman_to_numeral_map_ = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000},
    };
};

int main() {
    auto solution = Solution();

    assert(3 == solution.romanToInt("III"));
    assert(4 == solution.romanToInt("IV"));
    assert(9 == solution.romanToInt("IX"));
    assert(58 == solution.romanToInt("LVIII"));
    assert(1994 == solution.romanToInt("MCMXCIV"));
}
