#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 25
using namespace std;

int map[MAX][MAX];
bool visited[MAX][MAX] = {false,};
int N; // 지도의 크기
int change_x[4]={0, -1, 1, 0};
int change_y[4]={-1, 0, 0, 1};
int house = 0;

int dfs(int y, int x){
    house++;
    visited[y][x] = true;
    for(int i=0;i<4;i++){
        int nx = x + change_x[i];
        int ny = y + change_y[i];
        
        if(nx<0 || ny<0 || nx>=N ||ny>=N) continue;
        else if(map[ny][nx] == 1 && visited[ny][nx] == false)
            dfs(ny, nx);
    }
    
    return house;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
   
    vector<int> answer;
    cin >> N;
    
    for (int i=0; i<N; i++){
        string tmp;
        cin >> tmp;
        for(int j=0;j<N;j++){
            map[i][j]=tmp[j] - '0'; // char to int type
        }
    }
    
    for (int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if (visited[i][j] == false && map[i][j] == 1){
                house = 0;  // 집의 개수
                answer.push_back(dfs(i, j));
            }

        }
    }
    
    sort(answer.begin(), answer.end());
    
    cout<<answer.size()<<endl;
    
    for(int i=0; i<answer.size();i++)
        cout << answer.at(i)<< endl;
    
    return 0;
}
