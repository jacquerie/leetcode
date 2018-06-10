// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <stack>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    int calPoints(vector<string>& ops) {
        stack<int> points;

        for (auto op : ops) {
            if (op == "+") {
                int p2 = points.top();
                points.pop();
                int p1 = points.top();
                points.pop();
                points.push(p1);
                points.push(p2);
                points.push(p1 + p2);
            } else if (op == "C") {
                points.pop();
            } else if (op == "D") {
                int p = points.top();
                points.pop();
                points.push(p);
                points.push(2 * p);
            } else {
                points.push(stoi(op));
            }
        }

        int result = 0;

        while (!points.empty()) {
            result += points.top();
            points.pop();
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<string> ops = {"5", "2", "C", "D", "+"};

    assert(30 == solution.calPoints(ops));
}
