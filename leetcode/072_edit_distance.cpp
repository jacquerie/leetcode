// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    int minDistance(string word1, string word2) {
        int len1 = word1.size(), len2 = word2.size();
        vector<vector<int>> distances(len1 + 1, vector<int>(len2 + 1));

        distances[0][0] = 0;
        for (int i = 1; i <= len1; i++) {
            distances[i][0] = i;
        }
        for (int j = 1; j <= len2; j++) {
            distances[0][j] = j;
        }

        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                distances[i][j] = min({
                    distances[i - 1][j] + 1,
                    distances[i][j - 1] + 1,
                    distances[i - 1][j - 1] + (word1[i - 1] == word2[j - 1] ? 0 : 1),
                });
            }
        }

        return distances[len1][len2];
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.minDistance("horse", "ros"));
    assert(5 == solution.minDistance("intention", "execution"));
}
