// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <utility>
#include <vector>

using namespace std;

class MyCalendar {
 public:
    MyCalendar() {}

    bool book(int start, int end) {
        pair<int, int> new_event = {start, end};

        for (auto event : events_) {
            if (intersects(event, new_event)) {
                return false;
            }
        }

        events_.push_back(new_event);

        return true;
    }

 private:
    vector<pair<int, int>> events_;

    bool intersects(pair<int, int> a, pair<int, int> b) {
        return !((a.second <= b.first) || (b.second <= a.first));
    }
};

int main() {
    auto obj = MyCalendar();

    assert(obj.book(10, 20));
    assert(!obj.book(15, 25));
    assert(obj.book(20, 30));
}
