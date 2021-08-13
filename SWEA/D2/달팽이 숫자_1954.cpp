#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	 
	cin>>T;
	 
	for(test_case = 1; test_case <= T; ++test_case)
	{
      	int N;
        cin >> N;
        
        int board [N][N];
        for(int i=0; i<N;i++)
            for(int j=0; j<N; j++)
                board[i][j] = 0;
		
        int num = 1;
        int y=0, x=-1;
        
        for(int rnd=N-1; rnd>0; rnd-=2){	// 한 번의 round당 4개의 step이 이루어진다. rnd: 한 step의 숫자 길이
            for (int i=0; i<rnd*4; i++){
                if ((float)i/rnd <= 1) x++;		// step1. 우로 이동
                else if ((float)i/rnd <= 2) y++;	// step2. 아래로 이동
                else if ((float)i/rnd <= 3) x--;	// step3. 좌로 이동
                else y--;				// step4. 위로 이동
                board[y][x] = num++;
                
            }
        }
        
	// N이 홀수일 경우, 가운데 숫자가 빈다.
        if (num==N*N)
            board[y][++x] = num;


	// 출력	
        printf("#%d\n", test_case);
		for(int i=0; i<N;i++){
            for(int j=0; j<N; j++)
                printf("%d ", board[i][j]);
            cout<<endl;
        }
	}
	return 0; 
}
/*
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq
*/
