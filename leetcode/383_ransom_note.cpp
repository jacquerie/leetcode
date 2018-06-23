// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
 public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> ransomNoteCounter;
        for (auto c : ransomNote) {
            ransomNoteCounter[c]++;
        }

        unordered_map<char, int> magazineCounter;
        for (auto c : magazine) {
            magazineCounter[c]++;
        }

        for (auto pair : ransomNoteCounter) {
            auto it = magazineCounter.find(pair.first);
            if (it == magazineCounter.end() || pair.second > it->second) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    auto solution = Solution();

    assert(!solution.canConstruct("a", "b"));
    assert(!solution.canConstruct("aa", "ab"));
    assert(solution.canConstruct("aa", "aab"));
}
