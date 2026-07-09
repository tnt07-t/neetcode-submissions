class Solution {
public:
    vector<vector<string>> res;

    vector<vector<string>> solveNQueens(int n) {


        vector<string> board(n, string(n, '.'));
        backtrack(0,board);
        return res;
    }


private: 

    //check placement against above
    bool valid(int r,int c, vector<string>& board){
        int n = board.size();
        //up
        for (int i = r-1; i>=0 ; i--){
            if (board[i][c] == 'Q'){
                return false;
            }
        }
        //diagonal left
        for (int i = r-1, j = c-1; i >= 0 && j >=0; i--,j--){
            if (board[i][j] == 'Q'){
                return false;
            }
        }

        //hor-left
        for (int j = c-1; j >= 0; j--){
            if (board[r][j] == 'Q'){
                return false;
            }
        }
        // diagonal right
        for (int i = r - 1, j = c + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        return true;
    }

    void backtrack(int row, vector<string>& board){
        int n = board.size();
        if (row == n){
            res.push_back(board);
            return;
        }
        for (int c = 0; c < n; c++){ //try each position in row
            if (valid(row,c,board)){
                board[row][c] = 'Q';
                backtrack(row+1, board);
            }
            board[row][c] = '.';
        }
    }
};
