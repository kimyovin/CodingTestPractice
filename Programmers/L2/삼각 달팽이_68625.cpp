#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    vector<vector<int>> board(n, vector<int>(n, 0));
    
    int num = 1;    // 넣을 수
    int y = -1, x = 0;
    
    for(int rnd=0; rnd<n;rnd++){  // round: 회차
        for (int j=rnd; j<n; j++){
            if (rnd%3 ==0)
                y++;
            else if (rnd%3==1)
                x++;
            else {x--; y--;}
            board[y][x] = num++;
        }
    }
    for (int i=0;i<n; i++)
        for(int j=0; j<i+1; j++)
            answer.push_back(board[i][j]);
    
    return answer;
}

//https://programmers.co.kr/learn/courses/30/lessons/68645
