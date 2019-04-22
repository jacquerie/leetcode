// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <stack>
#include <string>

using namespace std;

class Solution {
 public:
    bool backspaceCompare(string S, string T) {
        return stringToStack(S) == stringToStack(T);
    }

 private:
     stack<char> stringToStack(string S) {
         stack<char> stack;

         for (auto c : S) {
             if (c == '#') {
                 if (!stack.empty()) {
                     stack.pop();
                 }
             } else {
                 stack.push(c);
             }
         }

         return stack;
     }
};

int main() {
    auto solution = Solution();

    assert(solution.backspaceCompare("ab#c", "ad#c"));
    assert(solution.backspaceCompare("ab##", "c#d#"));
    assert(solution.backspaceCompare("a##c", "#a#c"));
    assert(!solution.backspaceCompare("a#c", "b"));
}
