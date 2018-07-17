// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstdlib>

using namespace std;

class Solution {
 public:
    int rand10() {
        int x = 0, y = 0;

        while (!x || !y) {
            int roll = rand7();
            switch (roll) {
                case 1:
                case 2:
                    x = roll;
                    break;
                case 3:
                case 4:
                case 5:
                case 6:
                case 7:
                    y = roll;
                    break;
            }
        }

        return 5 * (x - 1) + (y - 2);
    }

 private:
    int rand7() {
        return rand() % 7 + 1;
    }
};

int main() {
    auto solution = Solution();

    assert(8 == solution.rand10());
}
