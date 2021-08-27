#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;

int answer=0; // 감염된 수

void dfs(int start, vector<int> graph[], bool visited[]){
    visited[start] = true;
    for(int i =0; i<graph[start].size(); i++){
        int next = graph[start][i];
        if(!visited[next]){     // 방문하지 않았다면
            dfs(next, graph, visited);
            answer++;
        }
    }    
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int node_num;
    int edge_num;
    cin >>node_num >> edge_num;

    bool visited[node_num+1];
    memset(visited, false, sizeof(visited));
    vector<int> graph[node_num+1];
    for(int i=0; i<edge_num; i++){
        int in, out;
        cin >> in >> out;
        graph[in].push_back(out);
        graph[out].push_back(in);   // 양방향 그래프
    }
    
    dfs(1, graph, visited);
    
    printf("%d", answer);
    
    return 0;
}

/*
https://www.acmicpc.net/problem/2606
*/
