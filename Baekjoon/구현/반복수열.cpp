#include <iostream>
#include <queue>
#include <cmath>

#define MAX 236196  //9^5 * 4
using namespace std;

int A, P;   // n가지 종류의 동전. k원의 가치
int num = 0;
int visited[MAX]={0,};

int bfs(int A, int P){
    queue<pair<int, int>> que;
    que.push(make_pair(A, 1));
    visited[A] = 1;
    while (!que.empty()) {
        int count = que.front().second;
        string tmp_n = to_string(que.front().first);
        que.pop();
        int next_n = 0;
        for(int i = tmp_n.size(); i>0; i--){
            next_n += pow(tmp_n.at(i-1) - '0', P);
        }
        
        if(visited[next_n] == 0){
            que.push(make_pair(next_n, count+1));
            visited[next_n] = count+1;
        }
        else{
            return visited[next_n]-1;
        }
            
    }
    return -1;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> A >> P;
    cout << bfs(A, P)<<endl;
    
    
    return 0;
}

// https://www.acmicpc.net/problem/2331
