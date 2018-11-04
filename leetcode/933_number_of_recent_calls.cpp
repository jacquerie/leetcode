// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <queue>

using namespace std;

class RecentCounter {
 public:
    RecentCounter(): count_(0), queue_() {}

    int ping(int t) {
        while (!queue_.empty() && (t - queue_.front() > 3000)) {
            count_--;
            queue_.pop();
        }

        count_++;
        queue_.push(t);

        return queue_.size();
    }

 private:
    int count_;
    queue<int> queue_;
};

int main() {
    auto obj = RecentCounter();

    assert(1 == obj.ping(1));
    assert(2 == obj.ping(100));
    assert(3 == obj.ping(3001));
    assert(3 == obj.ping(3002));
}
