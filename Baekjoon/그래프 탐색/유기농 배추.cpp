#include <iostream>

#define MAX 50
using namespace std;

int T, M, N, K;
int num;    // 벌레 개수

void dfs(int x, int y, int map[MAX][MAX], bool visited[MAX][MAX]){
    visited[x][y] = true;
    
    // 위로 이동
    if(0<=x-1 && !visited[x-1][y] &&map[x-1][y]==1)
        dfs(x-1, y, map, visited);
    // 좌로 이동
    if(0<=y-1 && !visited[x][y-1] &&map[x][y-1]==1)
        dfs(x, y-1, map, visited);
    // 우로 이동
    if(y+1<N && !visited[x][y+1]&&map[x][y+1]==1)
        dfs(x, y+1, map, visited);
    // 아래로 이동
    if(x+1<M && !visited[x+1][y]&&map[x+1][y]==1)
        dfs(x+1, y, map, visited);
    
    return;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> T;
    
    for(int i=0; i<T; i++){
        cin>> M>> N>> K;
        num = 0;
        bool visited[MAX][MAX]={false,};
        int map[MAX][MAX]={0,};

        for(int i=0; i<K;i++){
            int X, Y;
            cin >> X>> Y;
            map[X][Y]=1;
        }
        
        for(int x=0;x<M;x++){
            for(int y=0;y<N;y++){
                if(map[x][y]==1 &&!visited[x][y]){
                    dfs(x, y, map, visited);
                    num++;
                }
            }
        }
        
        cout << num<<endl;
    }
    
    return 0;
}

/********************************************
*
* 나의풀이2 - BFS로 구현
*
********************************************/

#include <string.h>
#include <iostream>
#include <queue>

#define MAX 50
using namespace std;

struct POS{
    int X, Y;
};
int T, M, N, K;
int map[MAX][MAX];

void bfs(int x_start, int y_start){
    queue<POS> que;
    que.push({x_start, y_start});
    
    map[x_start][y_start] = 2;   // (x, y)를 방문했다는 표시
    while(!que.empty()){
        int x = que.front().X;
        int y = que.front().Y;
        que.pop();
        
        // 위로 이동
        if (0<=y-1 && map[x][y-1]==1){
            que.push({x, y-1});
            map[x][y-1] = 2;
        }
        // 좌로 이동
        if (0<=x-1 && map[x-1][y]==1){
            que.push({x-1, y});
            map[x-1][y] = 2;
        }
        // 우로 이동
        if (y+1<N && map[x][y+1]==1){
            que.push({x, y+1});
            map[x][y+1] = 2;
        }
        // 아래로 이동
        if (x+1<M && map[x+1][y]==1){
            que.push({x+1, y});
            map[x+1][y] = 2;
        }
    }
    return ;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> T;
    
    for(int i=0; i<T; i++){
        cin>> M>> N>> K;
        int num=0;    // 벌레 개수
        
        memset(map, 0, sizeof(map));
        for(int i=0; i<K;i++){
            int X, Y;
            cin >> X>> Y;
            map[X][Y]=1;
        }
        
        for(int x=0;x<M;x++){
            for(int y=0;y<N;y++){
                if(map[x][y]==1){
                    bfs(x, y);
                    num++;
                }
            }
        }
        
        cout << num<<endl;
    }
    
    return 0;
}



// https://www.acmicpc.net/problem/1012
