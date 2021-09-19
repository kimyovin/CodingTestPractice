#include <iostream>
#include <vector>
#include <queue>

#define MAX 100001
using namespace std;

int N, K;   // N: 수빈이의 위치, K: 동생의 위치
bool visited[MAX]={false,};
int min_num=MAX;  // 최소 횟수

void bfs(int N, int K){
    queue<pair<int, int>> que;
    visited[N] = true;
    que.emplace(make_pair(N, 0));
    
    while(!que.empty()){
        int now = que.front().first;
        int num = que.front().second;
        que.pop();
        
        if(now == K){
            min_num = num;
            return;
        }
        
        visited[now] = true;
        
        if(now*2 <= K+1 && !visited[now*2])
            que.emplace(make_pair(now*2, num));
        if(0<=now-1 && !visited[now-1])
            que.emplace(make_pair(now-1, num+1));
        if(now+1 <= K && !visited[now+1])
            que.emplace(make_pair(now+1, num+1));
        
    }
    return;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> N >> K;
    bfs(N, K);
    printf("%d\n", min_num);
    
    return 0;
}
// https://www.acmicpc.net/problem/13549
