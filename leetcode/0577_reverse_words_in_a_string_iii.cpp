// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    string reverseWords(string s) {
        int i = -1;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == ' ') {
                if (i != -1) {
                    reverseWords(s, i, j - 1);
                    i = -1;
                }
            } else if (j == s.length() - 1) {
                if (i != -1) {
                    reverseWords(s, i, j);
                    i = -1;
                }
            } else {
                if (i == -1) {
                    i = j;
                }
            }
        }

        return s;
    }

 private:
    void reverseWords(string& s, int i, int j) {
        while (i < j) {
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;

            i++;
            j--;
        }
    }
};

int main() {
    auto solution = Solution();

    assert("s'teL ekat edoCteeL tsetnoc" == solution.reverseWords("Let's take LeetCode contest"));
}
