#include<iostream>
 
using namespace std;
int values[1000000];

int main(int argc, char** argv)
{
    int test_case;
    int T;
 
    cin>>T;
 
    for(test_case = 1; test_case <= T; ++test_case)
    {
        int N;
        long long total=0;
        scanf("%d", &N);
          
        for (int i = 0; i < N; i++){
            scanf("%d", values+i);
        }
        int _max = values[N-1];
 
        for (int i=N-2; i>=0; i--){ 
            if (values[i] > _max)
                _max = values[i];
            else
                total += _max - values[i];
        }
//      cout << "#" << test_case << " " << total << endl;
        printf("#%d %lld\n", test_case, total);
    }
    return 0;
}

/*
자연수 N(2 ≤ N ≤ 1,000,000)
각 날의 매매가 : 10,000 이하

매매가가 계속 1이었다가 1,000,000날에 10,000원이라면
total = 999,999 * 9999 = 9,998,990,001 이 되므로 unsigned int의 최댓값인 4,294,967,295 보다 크다.

따라서 total을 long long 타입으로 설정해야한다.

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
*/
