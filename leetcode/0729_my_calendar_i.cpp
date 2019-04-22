// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <map>

using namespace std;

class MyCalendar {
 public:
    MyCalendar() {}

    bool book(int start, int end) {
        auto next = events_.lower_bound(start);
        if (next != events_.end() && next->first < end) {
            return false;
        } else if (next != events_.begin() && start < (--next)->second) {
            return false;
        }

        events_[start] = end;

        return true;
    }

 private:
    map<int, int> events_;
};

int main() {
    auto obj = MyCalendar();

    assert(obj.book(10, 20));
    assert(!obj.book(15, 25));
    assert(obj.book(20, 30));
}
