#include <iostream>
#include <algorithm>

using namespace std;

int solution(int price[][3], int N){
    for(int i=1; i<N; i++){
        price[i][0] += min(price[i-1][1], price[i-1][2]);
        price[i][1] += min(price[i-1][0], price[i-1][2]);
        price[i][2] += min(price[i-1][0], price[i-1][1]);
    }
    
    return *min_element(&price[N-1][0], &price[N-1][0]+3);
}

int main(int argc, const char * argv[]) {
    
    int N; // 집 개수
    cin >> N;
    int price[N][3];
    
    //input
    for(int i=0; i<N; i++){
        cin >> price[i][0] >> price[i][1] >> price[i][2];
    }
    
    printf("%d\n", solution(price, N));
    
    
    return 0;
}

// https://www.acmicpc.net/problem/1149
