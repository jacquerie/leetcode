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

        for (int i = 0; i < len1 + 1; i++) {
            for (int j = 0; j < len2 + 1; j++) {
                if (i == 0 && j == 0) {
                    distances[i][j] = 0;
                } else if (i == 0) {
                    distances[i][j] = j;
                } else if (j == 0) {
                    distances[i][j] = i;
                } else {
                    distances[i][j] = min({
                        distances[i - 1][j] + 1,
                        distances[i][j - 1] + 1,
                        distances[i - 1][j - 1] + (word1[i - 1] == word2[j - 1] ? 0 : 1),
                    });
                }
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
