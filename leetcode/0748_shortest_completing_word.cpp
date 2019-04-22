// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cctype>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
    string shortestCompletingWord(string licensePlate, vector<string> words) {
        string result;

        auto licensePlateCounts = toCounts(licensePlate);
        for (auto word : words) {
            auto wordCounts = toCounts(word);
            if (isContained(licensePlateCounts, wordCounts) && (result.empty() || word.size() < result.size())) {
                result = word;
            }
        }

        return result;
    }

 private:
    unordered_map<char, int> toCounts(const string word) {
        unordered_map<char, int> result;

        for (auto c : word) {
            if (isalpha(c)) {
                result[tolower(c)]++;
            }
        }

        return result;
    }

    bool isContained(unordered_map<char, int> firstWordCounts, unordered_map<char, int> secondWordCounts) {
        for (auto it : firstWordCounts) {
            if (secondWordCounts[it.first] < it.second) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    auto solution = Solution();

    string licensePlate = "1s3 PSt";
    vector<string> words = {"step", "steps", "strip", "stepple"};

    string expected = "steps";
    string result = solution.shortestCompletingWord(licensePlate, words);

    assert(expected == result);
}
