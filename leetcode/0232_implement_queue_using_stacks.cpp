// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <stack>

using namespace std;

class MyQueue {
 public:
    MyQueue() {}

    void push(int x) {
        stack1_.push(x);
    }

    int pop() {
        peek();
        int tmp = stack2_.top();
        stack2_.pop();
        return tmp;
    }

    int peek() {
        if (stack2_.empty()) {
            while (!stack1_.empty()) {
                int tmp = stack1_.top();
                stack1_.pop();
                stack2_.push(tmp);
            }
        }
        return stack2_.top();
    }

    bool empty() {
        return stack1_.empty() && stack2_.empty();
    }

 private:
    stack<int> stack1_, stack2_;
};

int main() {
    auto obj = MyQueue();

    obj.push(1);
    obj.push(2);
    assert(1 == obj.peek());
    assert(1 == obj.pop());
    assert(!obj.empty());
}
