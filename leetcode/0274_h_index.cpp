// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int hIndex(vector<int>& citations) {
        int length = citations.size();

        vector<int> histogram(length + 1);
        for (auto citation : citations) {
            histogram[min(citation, length)]++;
        }

        int sum = 0;
        for (int i = length; i >= 0; i--) {
            sum += histogram[i];
            if (sum >= i) {
                return i;
            }
        }

        return 0;
    }
};

int main() {
    auto solution = Solution();

    vector<int> citations = {3, 0, 6, 1, 5};

    assert(3 == solution.hIndex(citations));
}
