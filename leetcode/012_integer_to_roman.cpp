// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
    string intToRoman(int num) {
        string result;

        for (auto element : numeral_roman_map) {
            while (num >= element.first) {
                result += element.second;
                num -= element.first;
            }
        }

        return result;
    }

 private:
    const vector<pair<int, string>> numeral_roman_map = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"},
    };
};

int main() {
    auto solution = Solution();

    assert("III" == solution.intToRoman(3));
    assert("IV" == solution.intToRoman(4));
    assert("IX" == solution.intToRoman(9));
    assert("LVIII" == solution.intToRoman(58));
    assert("MCMXCIV" == solution.intToRoman(1994));
}
