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
		scanf("%d", &N);
        int sum=0;
        for (int i = 1; i <= N; i++){
        	sum += (i%2==0? -i: i);
        }
        printf("#%d %d\n", test_case, sum);
	}
	return 0;
}
