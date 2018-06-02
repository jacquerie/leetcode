#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int countBattleships(vector<vector<char>>& board) {
        int result = 0;
        if (board.empty() || board[0].empty()) {
            return result;
        }

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == 'X' &&
                    (i == 0 || board[i - 1][j] != 'X') &&
                    (j == 0 || board[i][j - 1] != 'X')) {
                   result++;
                }
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<char>> board = {
        {'X', '.', '.', 'X'},
        {'.', '.', '.', 'X'},
        {'.', '.', '.', 'X'},
    };

    assert(2 == solution.countBattleships(board));
}
