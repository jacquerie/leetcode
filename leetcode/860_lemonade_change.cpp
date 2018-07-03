// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool lemonadeChange(vector<int>& bills) {
        int fives = 0, tens = 0;

        for (auto bill : bills) {
            if (bill == 5) {
                fives++;
            } else if (bill == 10) {
                if (fives > 0) {
                    fives--;
                    tens++;
                } else {
                    return false;
                }
            } else {
                if (fives > 0 && tens > 0) {
                    fives--;
                    tens--;
                } else if (fives >= 3) {
                    fives -= 3;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
};

int main() {
    auto solution = Solution();

    vector<int> bills = {5, 5, 5, 10, 20};

    assert(solution.lemonadeChange(bills));
}
