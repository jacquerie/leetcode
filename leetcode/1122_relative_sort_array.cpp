// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> result(arr1.begin(), arr1.end());

        unordered_map<int, int> ranks = toRanks(arr2);
        sort(result.begin(), result.end(), [&ranks](int x, int y) {
            if (ranks.find(x) != ranks.end() && ranks.find(y) != ranks.end()) {
                return ranks.at(x) < ranks.at(y);
            } else if (ranks.find(x) != ranks.end()) {
                return true;
            } else if (ranks.find(y) != ranks.end()) {
                return false;
            } else {
                return x < y;
            }
        });

        return result;
    }

 private:
    unordered_map<int, int> toRanks(vector<int>& arr) {
        unordered_map<int, int> result;

        for (int i = 0; i < arr.size(); i++) {
            result[arr[i]] = i;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> arr1 = {2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19};
    vector<int> arr2 = {2, 1, 4, 3, 9, 6};

    vector<int> expected = {2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19};
    vector<int> result = solution.relativeSortArray(arr1, arr2);

    assert(expected == result);
}
