// Copyright (c) 2020 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    int subtractProductAndSum(int n) {
        int prod = 1, sum = 0;
        while (n) {
            prod *= n % 10;
            sum += n % 10;
            n /= 10;
        }
        return prod - sum;
    }
};

int main() {
    auto solution = Solution();

    assert(15 == solution.subtractProductAndSum(234));
    assert(21 == solution.subtractProductAndSum(4421));
}
