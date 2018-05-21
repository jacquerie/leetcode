#include <cassert>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> partitionLabels (string S) {
        map<char, int> lastOccurrences;
        for (size_t i = 0; i < S.length(); i++) {
            lastOccurrences[S[i]] = i;
        }

        vector<int> result;
        size_t currentCharLast, currentFirst = 0, currentLast = 0;

        for (size_t i = 0; i < S.length(); i++) {
            currentCharLast = lastOccurrences[S[i]];
            currentLast = max(currentLast, currentCharLast);
            if (i == currentLast) {
                result.push_back(i - currentFirst + 1);
                currentFirst = i + 1;
            }
        }

        return result;
    }
};

int main () {
    auto solution = Solution();

    vector<int> expected = {9, 7, 8};
    vector<int> result = solution.partitionLabels("ababcbacadefegdehijhklij");

    assert(expected == result);
}
