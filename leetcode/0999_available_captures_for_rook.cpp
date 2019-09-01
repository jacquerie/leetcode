// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int numRookCaptures(vector<vector<char>>& board) {
        int result = 0;

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == 'R') {
                    result += numRookCaptures(board, i, j);
                }
            }
        }

        return result;
    }

 private:
    int numRookCaptures(vector<vector<char>>& board, int i, int j) {
        int result = 0;

        for (int k = i; k >= 0; k--) {
            if (board[k][j] == 'p') {
                result++;
                break;
            } else if (board[k][j] == 'B') {
                break;
            }
        }

        for (int k = i; k < board.size(); k++) {
            if (board[k][j] == 'p') {
                result++;
                break;
            } else if (board[k][j] == 'B') {
                break;
            }
        }

        for (int k = j; k >= 0; k--) {
            if (board[i][k] == 'p') {
                result++;
                break;
            } else if (board[i][k] == 'B') {
                break;
            }
        }

        for (int k = j; k < board[0].size(); k++) {
            if (board[i][k] == 'p') {
                result++;
                break;
            } else if (board[i][k] == 'B') {
                break;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<char>> board = {
        {'.', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '.', '.', 'p', '.', '.', '.', '.'},
        {'.', '.', '.', 'R', '.', '.', '.', 'p'},
        {'.', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '.', '.', 'p', '.', '.', '.', '.'},
        {'.', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '.', '.', '.', '.', '.', '.', '.'},
    };

    assert(3 == solution.numRookCaptures(board));
}
