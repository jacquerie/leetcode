#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int mid, first = 0, last = n - 1;

        while (first <= last) {
            mid = (first + last) / 2;
            if (citations[mid] >= n - mid) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return n - first;
    }
};

int main() {
    auto solution = Solution();

    vector<int> citations = {0, 1, 3, 5, 6};

    assert(3 == solution.hIndex(citations));
}
