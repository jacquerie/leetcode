// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;

        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                result.push_back("FizzBuzz");
            } else if (i % 5 == 0) {
                result.push_back("Buzz");
            } else if (i % 3 == 0) {
                result.push_back("Fizz");
            } else {
                result.push_back(to_string(i));
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<string> expected = {
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    };
    vector<string> result = solution.fizzBuzz(15);

    assert(expected == result);
}
