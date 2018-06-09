// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
    string findReplaceString(string S, vector<int>& indexes, vector<string>& sources, vector<string>& targets) {
        unordered_map<int, pair<int, string>> operations;
        for (int i = 0; i < indexes.size(); i++) {
            if (S.find(sources[i], indexes[i]) == indexes[i]) {
                operations[indexes[i]] = pair<int, string>(sources[i].length(), targets[i]);
            }
        }

        string result;

        int i = 0;
        while (i < S.length()) {
            if (operations.find(i) != operations.end()) {
                result += operations[i].second;
                i += operations[i].first;
            } else {
                result.push_back(S[i]);
                i++;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> indexes = {0, 2};
    vector<string> sources = {"a", "cd"};
    vector<string> targets = {"eee", "ffff"};

    assert("eeebffff" == solution.findReplaceString("abcd", indexes, sources, targets));
}
