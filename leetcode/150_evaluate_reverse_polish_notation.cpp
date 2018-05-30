#include <cassert>
#include <stack>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int evalRPN (vector<string>& tokens) {
        stack<int> stack;

        for (auto token : tokens) {
            int op1, op2;

            if (token == "+") {
                op2 = stack.top();
                stack.pop();
                op1 = stack.top();
                stack.pop();
                stack.push(op1 + op2);
            } else if (token == "-") {
                op2 = stack.top();
                stack.pop();
                op1 = stack.top();
                stack.pop();
                stack.push(op1 - op2);
            } else if (token == "*") {
                op2 = stack.top();
                stack.pop();
                op1 = stack.top();
                stack.pop();
                stack.push(op1 * op2);
            } else if (token == "/") {
                op2 = stack.top();
                stack.pop();
                op1 = stack.top();
                stack.pop();
                stack.push(op1 / op2);
            } else {
                stack.push(stoi(token));
            }
        }

        return stack.top();
    }
};

int main () {
    auto solution = Solution();

    vector<string> tokens = {"2", "1", "+", "3", "*"};

    assert(9 == solution.evalRPN(tokens));
}
