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
            if (numRookCaptures(board, k, j, result)) {
                break;
            }
        }

        for (int k = i; k < board.size(); k++) {
            if (numRookCaptures(board, k, j, result)) {
                break;
            }
        }

        for (int k = j; k >= 0; k--) {
            if (numRookCaptures(board, i, k, result)) {
                break;
            }
        }

        for (int k = j; k < board[0].size(); k++) {
            if (numRookCaptures(board, i, k, result)) {
                break;
            }
        }

        return result;
    }

    bool numRookCaptures(vector<vector<char>>& board, int i, int j, int& result) {
        if (board[i][j] == 'p') {
            result++;
            return true;
        } else if (board[i][j] == 'B') {
            return true;
        }

        return false;
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
