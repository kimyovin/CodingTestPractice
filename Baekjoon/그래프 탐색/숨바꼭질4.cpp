#include <iostream>
#include <vector>
#include <queue>

#define MAX 100001
using namespace std;

int N, K;   // N: 수빈이의 위치, K: 동생의 위치
bool visited[MAX]={false,};
int min_num=MAX;  // 최소 횟수
int selected[MAX]={-1,};
vector<int> route;

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
            for(int i=K; i !=N; i = selected[i]){
                route.push_back(i);
            }
            route.push_back(N);
            return;
        }
        
        if(now*2 <= K+1 && !visited[now*2]){
            que.emplace(make_pair(now*2, num+1));
            selected[now*2] = now;
            visited[now*2] = true;
        }
        if(0<=now-1 && !visited[now-1]){
            que.emplace(make_pair(now-1, num+1));
            selected[now-1] = now;
            visited[now-1] = true;
        }
        if(now+1 <= K && !visited[now+1]){
            que.emplace(make_pair(now+1, num+1));
            selected[now+1] = now;
            visited[now+1] = true;
        }
        
    }
}

int main(int argc, const char * argv[]) {
    cin >> N >> K;
    
    bfs(N, K);
    printf("%d\n", min_num);
    
     for(int i = route.size() - 1; i>=0; i--)
        cout<<route.at(i)<<' ';
    cout << endl;
    return 0;
}
