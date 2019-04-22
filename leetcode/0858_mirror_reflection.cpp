// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    int mirrorReflection(int p, int q) {
        int g = gcd(p, q);

        if ((p / g) % 2 && (q / g) % 2) {
            return 1;
        } else if ((p / g) % 2) {
            return 0;
        } else {
            return 2;
        }
    }

 private:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
};

int main() {
    auto solution = Solution();

    assert(2 == solution.mirrorReflection(2, 1));
}
