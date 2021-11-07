#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    int N;
    cin >> N;
    
    int cnt[N+1];
    cnt[0] = 1;
    cnt[1] = 1;
    
    for(int i=2; i<=N; i++){
        cnt[i] = (cnt[i-1] + cnt[i-2])%15746;
    }
    
    cout << cnt[N] <<endl;
    
    
    return 0;
}

// https://www.acmicpc.net/problem/1904
