#include <iostream>

#define MAX 1001    // 정답은 무조건 1000보단 아래
using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    cin >> N;
    int A[N];
    
    for(int i=0; i<N; i++){
        cin >> A[i];
    }
    
    int s[MAX];  // s[i]는 a[i]가 S_k일때의 좌측 오름차순 배열의 최대길이
    int e[MAX];  // s[i]는 a[i]가 S_k일때의 우측 내림차순 배열의 최대길이
    
    fill(s, s+MAX, 1);
    fill(e, e+MAX, 1);
    
    //s[] 배열 만들기
    for(int i=1; i<N; i++){
        for(int j=i-1; j>=0; j--){
            if(A[j] < A[i]) // 갱신
                s[i] = max(s[i], s[j]+1);
        }
    }
    
    //e[] 배열 만들기
    for(int i=N-2; i>=0; i--){
        for(int j=i+1; j<N; j++){
            if(A[i]>A[j])
                {
                    e[i] = max(e[i], e[j]+1);
                }
        }
    }
    
    int max_l = 0;
    
    for (int i=0; i<N; i++){
        int i_len = s[i]+e[i]-1;
        if(max_l < i_len)
            max_l = i_len;
    }
    
    cout <<max_l<<endl;
    
    
    return 0;
}

// https://www.acmicpc.net/problem/11054
