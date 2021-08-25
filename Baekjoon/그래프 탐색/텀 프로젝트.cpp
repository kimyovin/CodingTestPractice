#include <vector>
#include <iostream>
#include <stdio.h>
using namespace std;
int answer;

void dfs(int start_p, int start, int selected[], bool end[], bool visited[]){
    
    visited[start] = true;
    int next = selected[start];
    
    if(visited[next] == false)
        dfs(start_p, next, selected, end, visited);
    else // 이전에 방문했었던 점이라면
        if(end[next] == false){
            for (int i = next; i != start; i = selected[i]) {
                answer++;
            }
            answer++;
        }
    
    end[start] = true;
    
}

int main(int argc, const char * argv[]) {
  
    int test_case;
    int T;
     
    cin>>T;
     
    for(test_case = 1; test_case <= T; ++test_case)
    {
        answer = 0;
        int n;
        cin>>n;
        
        int selected[n+1];
        bool visited[n+1];
        bool end[n+1];
        
        fill(visited, visited+n+1, false);
        fill(end, end+n+1, false);
        
        for(int i=1; i<n+1; i++){
            cin >> selected[i];
        }
        
        for(int i=1; i<n+1; i++){
            if(visited[i] == false)
                dfs(i, i, selected, end, visited);
        }
        
        printf("%d\n", n-answer);
    }   
            
    return 0;
}

/*
end : 확인이 끝난 노드 배열

https://www.acmicpc.net/problem/9466
*/
