#include <iostream>
#include <queue>

#define MAX 10000
using namespace std;

int n, k;   // n가지 종류의 동전. k원의 가치
int num = 0;
bool visited[MAX] = {false,};
int bfs(vector<int> type){
    queue<pair<int, int>> que;
    que.push({0, 0});
    
    while(!que.empty()){
        int n_value = que.front().first;
        int n_num = que.front().second;
        que.pop();
        
        if(n_value == k){
            num = n_num;
            return n_num;
        }
        
        for(int i=0; i<type.size(); i++){
            int nx_value = n_value + type.at(i);
            if(nx_value<=k && !visited[nx_value]){
                que.push(make_pair(nx_value, n_num+1));
                visited[nx_value]=true;
            }
        }
    }
    
    return -1;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    vector<int> type;   // 동전의 종류
    cin >> n >> k;
    
    for(int i=0; i<n; i++){
        int coin;
        cin >> coin;
        type.push_back(coin);
    }
    
    cout << bfs(type) <<endl;
    
    
    return 0;
}


// DP에 속해있었지만 BFS로 최소 동전의 개수를 구하였다.
// https://www.acmicpc.net/problem/2294
