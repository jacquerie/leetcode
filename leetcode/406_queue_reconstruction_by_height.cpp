#include <algorithm>
#include <cassert>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        vector<pair<int, int>> result;

        sort(people.begin(), people.end(), [](pair<int, int>& p1, pair<int, int>& p2) {
            if (p2.first == p1.first) {
                return p1.second < p2.second;
            } else {
                return p2.first < p1.first;
            }
        });

        for (auto person : people) {
            result.emplace(result.begin() + person.second, person);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<pair<int, int>> people = {{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}};

    vector<pair<int, int>> expected = {{5, 0}, {7, 0}, {5, 2}, {6, 1}, {4, 4}, {7, 1}};
    vector<pair<int, int>> result = solution.reconstructQueue(people);

    assert(expected == result);
}
