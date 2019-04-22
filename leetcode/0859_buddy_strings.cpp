// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
    bool buddyStrings(string A, string B) {
        if (A.length() != B.length()) {
            return false;
        }

        int number_of_differences = 0;
        vector<pair<char, char>> differences;
        unordered_set<char> distinct;

        for (int i = 0; i < A.length(); i++) {
            if (A[i] == B[i]) {
                distinct.insert(A[i]);
                continue;
            }

            number_of_differences++;
            if (number_of_differences > 2) {
                return false;
            }

            differences.push_back(make_pair(A[i], B[i]));
        }

        if (number_of_differences == 0) {
            return distinct.size() < A.size();
        } else {
            return
                differences[0].first == differences[1].second &&
                differences[0].second == differences[1].first;
        }
    }
};

int main() {
    auto solution = Solution();

    assert(solution.buddyStrings("ab", "ba"));
    assert(!solution.buddyStrings("ab", "ab"));
    assert(solution.buddyStrings("aa", "aa"));
    assert(solution.buddyStrings("aaaaaaabc", "aaaaaaacb"));
    assert(!solution.buddyStrings("", "aa"));
}
