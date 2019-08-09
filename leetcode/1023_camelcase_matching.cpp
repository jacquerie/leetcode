// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <cctype>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        vector<bool> result;

        for (int i = 0; i < queries.size(); i++) {
            result.push_back(camelMatch(queries[i], pattern));
        }

        return result;
    }

 private:
    bool camelMatch(string query, string pattern) {
        int j = 0;

        for (int i = 0; i < query.length(); i++) {
            if (query[i] == pattern[j]) {
                j++;
            } else if (!islower(query[i])) {
                return false;
            }
        }

        return j == pattern.length();
    }
};

int main() {
    auto solution = Solution();

    vector<string> queries = {
        "FooBar",
        "FooBarTest",
        "FootBall",
        "FrameBuffer",
        "ForceFeedBack",
    };

    vector<bool> expected = {
        true,
        false,
        true,
        true,
        false,
    };
    vector<bool> result = solution.camelMatch(queries, "FB");

    assert(expected == result);
}
