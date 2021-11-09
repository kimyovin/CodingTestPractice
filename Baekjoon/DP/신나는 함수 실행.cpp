#include <iostream>

using namespace std;
int cnt[21][21][21]={0,};

int w(int a, int b, int c){
    if(a<=0 || b<=0 || c<=0)
        return 1;
    else if (a>20 || b>20 || c>20)
        return cnt[20][20][20] = w(20, 20, 20);
    
    else if(cnt[a][b][c] != 0)   // 이미 계산되었다면
        return cnt[a][b][c];
    
    else if ( a<b && b<c)
        cnt[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
    else
        cnt[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
    
    return cnt[a][b][c];
}

int main(int argc, const char * argv[]) {    
    int a, b, c;
    while (1){
        cin >> a >> b >> c;
        if(a == -1 && b==-1 && c==-1)
            break;
        
        printf("w(%d, %d, %d) = %d\n", a, b, c, w(a,b,c));
        
    }
    
    
    return 0;
}

// https://www.acmicpc.net/problem/9184
