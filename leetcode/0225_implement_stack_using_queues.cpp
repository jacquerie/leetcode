// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <queue>

using namespace std;

class MyStack {
 public:
    MyStack() {}

    void push(int x) {
        queue_.push(x);
        for (int i = 0; i < queue_.size() - 1; i++) {
            int tmp = queue_.front();
            queue_.pop();
            queue_.push(tmp);
        }
    }

    int pop() {
        int tmp = queue_.front();
        queue_.pop();
        return tmp;
    }

    int top() {
        return queue_.front();
    }

    bool empty() {
        return queue_.empty();
    }

 private:
    queue<int> queue_;
};

int main() {
    auto obj = MyStack();

    obj.push(1);
    obj.push(2);
    assert(2 == obj.top());
    assert(2 == obj.pop());
    assert(!obj.empty());
}
