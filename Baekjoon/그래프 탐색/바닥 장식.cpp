#include <iostream>
#define MAX 100
using namespace std;

int N, M;
bool visited[MAX][MAX]={false,};
char map[MAX][MAX];
int ws_count=0;

void dfs(int y, int x, char _char){
    visited[y][x] = true;
    char nchar = map[y][x];
    
    if(_char == nchar){
        if(nchar == '-' && !visited[y][++x] && x<M)
            dfs(y, x, nchar);
        else if (nchar == '|' && !visited[++y][x] && y<N)
            dfs(y, x, nchar);
    }
    else visited[y][x]=false;
    return;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> N >> M;
    
    for(int i=0; i<N; i++){
        string tmp;
        cin >> tmp;
        for(int j=0;j<M;j++){
            map[i][j]=tmp[j];
        }
    }
    
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++)
            if(!visited[i][j]){
                dfs(i, j, map[i][j]);
                ws_count++;
            }
    }
    
    cout << ws_count<<endl;
    return 0;
}

// https://www.acmicpc.net/problem/1388
