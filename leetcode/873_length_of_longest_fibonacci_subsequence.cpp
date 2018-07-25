// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
 public:
    int lenLongestFibSubseq(vector<int>& A) {
        int result = 2;

        unordered_set<int> setA(A.begin(), A.end());
        for (int i = 0; i < A.size() - 1; i++) {
            for (int j = i + 1; j < A.size(); j++) {
                int x = A[i], y = A[j], partial = 2;
                while (setA.find(x + y) != setA.end()) {
                    y = x + y;
                    x = y - x;
                    partial++;
                }
                result = max(result, partial);
            }
        }

        return result > 2 ? result : 0;
    }
};

int main() {
    auto solution = Solution();

    vector<int> A = {1, 2, 3, 4, 5, 6, 7, 8};

    assert(5 == solution.lenLongestFibSubseq(A));
}
