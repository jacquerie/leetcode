// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
    int countCharacters(vector<string>& words, string chars) {
        int result = 0;

        unordered_map<char, int> charCounts = toCharCounts(chars);
        for (const auto& word : words) {
            if (canConstruct(word, charCounts)) {
                result += word.length();
            }
        }

        return result;
    }

 private:
    unordered_map<char, int> toCharCounts(string chars) {
        unordered_map<char, int> result;

        for (const auto& c : chars) {
            result[c]++;
        }

        return result;
    }

    bool canConstruct(string word, unordered_map<char, int> charCounts) {
        for (const auto& c : word) {
            charCounts[c]--;
            if (charCounts[c] < 0) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    auto solution = Solution();

    vector<string> words = {"cat", "bt", "hat", "tree"};

    assert(6 == solution.countCharacters(words, "atach"));
}
