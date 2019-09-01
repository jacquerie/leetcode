// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> result;

        vector<string> words = toWords(text);
        for (int i = 0; i < words.size() - 2; i++) {
            if (words[i] == first && words[i + 1] == second) {
                result.push_back(words[i + 2]);
            }
        }

        return result;
    }

 private:
    vector<string> toWords(string text) {
        vector<string> result;

        string word = "";
        for (const auto& c : text) {
            if (c == ' ') {
                result.push_back(word);
                word = "";
            } else {
                word.push_back(c);
            }
        }
        result.push_back(word);

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<string> expected = {"girl", "student"};
    vector<string> result = solution.findOcurrences("alice is a good girl she is a good student", "a", "good");

    assert(expected == result);
}
