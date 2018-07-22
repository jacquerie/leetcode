// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <vector>

using namespace std;

enum Orientation {
    NORTH,
    EAST,
    SOUTH,
    WEST,
};

class Solution {
 public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<int> obstacles_;
        for (auto obstacle : obstacles) {
            obstacles_.insert(32768 * obstacle[0] + obstacle[1]);
        }

        Orientation orientation = NORTH;
        int current_x = 0, current_y = 0, result = 0;

        for (auto command : commands) {
            switch (command) {
                case -2:
                    switch (orientation) {
                        case NORTH:
                            orientation = WEST;
                            break;
                        case EAST:
                            orientation = NORTH;
                            break;
                        case SOUTH:
                            orientation = EAST;
                            break;
                        case WEST:
                            orientation = SOUTH;
                            break;
                    }
                    break;
                case -1:
                    switch (orientation) {
                        case NORTH:
                            orientation = EAST;
                            break;
                        case EAST:
                            orientation = SOUTH;
                            break;
                        case SOUTH:
                            orientation = WEST;
                            break;
                        case WEST:
                            orientation = NORTH;
                            break;
                    }
                    break;
                default:
                    for (int i = 0; i < command; i++) {
                        int next_x = current_x, next_y = current_y;
                        switch (orientation) {
                            case NORTH:
                                next_y++;
                                break;
                            case EAST:
                                next_x++;
                                break;
                            case SOUTH:
                                next_y--;
                                break;
                            case WEST:
                                next_x--;
                                break;
                        }

                        if (obstacles_.find(32768 * next_x + next_y) == obstacles_.end()) {
                            current_x = next_x;
                            current_y = next_y;
                        }

                        result = max(result, getDistance(current_x, current_y));
                    }
            }
        }

        return result;
    }

 private:
    int getDistance(int x, int y) {
        return x * x + y * y;
    }
};

int main() {
    auto solution = Solution();

    vector<int> commands = {4, -1, 4, -2, 4};
    vector<vector<int>> obstacles = {{2, 4}};

    assert(65 == solution.robotSim(commands, obstacles));
}
