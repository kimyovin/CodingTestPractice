#include <iostream>

using namespace std;
long long mem[101]={0,};

long P(int n){
    if(mem[n] != 0){
        return mem[n];
    }
    
    for(int i=7; i<=n; i++){
        mem[i] = mem[i-1] + mem[i-5];
    }
    
    return mem[n];
}

int main(int argc, const char * argv[]) {
    mem[1]=mem[2]=mem[3]= 1;
    mem[4]=mem[5]= 2;
    mem[6]= 3;
    
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N;
        cin >> N;
        cout << P(N)<<endl;
    }
    
    return 0;
}

// https://www.acmicpc.net/problem/9461
