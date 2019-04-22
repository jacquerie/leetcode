// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <unordered_map>

using namespace std;

class Solution {
 public:
    bool reorderedPowerOf2(int N) {
        auto countsN = toCounts(N);

        for (int i = 0; i < 32; i++) {
            auto countsM = toCounts(1 << i);
            if (countsM == countsN) {
                return true;
            }
        }

        return false;
    }

 private:
    unordered_map<int, int> toCounts(int n) {
        unordered_map<int, int> result;

        while (n) {
            result[n % 10]++;
            n /= 10;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.reorderedPowerOf2(1));
    assert(!solution.reorderedPowerOf2(10));
    assert(solution.reorderedPowerOf2(16));
    assert(!solution.reorderedPowerOf2(24));
    assert(solution.reorderedPowerOf2(46));
    assert(solution.reorderedPowerOf2(46));
}
