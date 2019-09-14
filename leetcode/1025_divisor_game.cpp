// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool divisorGame(int N) {
        vector<bool> result(N + 1);

        for (int i = 2; i <= N; i++) {
            for (int j = 1; j < i; j++) {
                if (i % j == 0 && !result[i - j]) {
                    result[i] = true;
                }
            }
        }

        return result[N];
    }
};

int main() {
    auto solution = Solution();

    assert(solution.divisorGame(2));
    assert(!solution.divisorGame(3));
}
