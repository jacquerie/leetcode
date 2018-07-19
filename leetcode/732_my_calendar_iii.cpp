// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <map>

using namespace std;

class MyCalendarThree {
 public:
    MyCalendarThree() {}

    int book(int start, int end) {
        events_[start]++;
        events_[end]--;

        int count = 0, result = 0;

        for (auto event : events_) {
            count += event.second;
            result = max(result, count);
        }

        return result;
    }

 private:
    map<int, int> events_;
};

int main() {
    auto obj = MyCalendarThree();

    assert(1 == obj.book(10, 20));
    assert(1 == obj.book(50, 60));
    assert(2 == obj.book(10, 40));
    assert(3 == obj.book(5, 15));
    assert(3 == obj.book(5, 10));
    assert(3 == obj.book(25, 55));
}
