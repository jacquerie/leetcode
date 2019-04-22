// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <stack>

using namespace std;

class MinStack {
 public:
    MinStack() {}

    void push(int x) {
        if (mins_.empty() || x <= mins_.top()) {
            mins_.push(x);
        }
        stack_.push(x - mins_.top());
    }

    void pop() {
        if (!stack_.top()) {
            mins_.pop();
        }
        stack_.pop();
    }

    int top() {
        return mins_.top() + stack_.top();
    }

    int getMin() {
        return mins_.top();
    }

 private:
    stack<int> mins_;
    stack<int> stack_;
};

int main() {
    auto obj = MinStack();

    obj.push(-2);
    obj.push(0);
    obj.push(-3);
    assert(-3 == obj.getMin());
    obj.pop();
    assert(0 == obj.top());
    assert(-2 == obj.getMin());
}
