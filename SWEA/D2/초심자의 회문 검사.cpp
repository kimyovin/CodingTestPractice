#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
		char word[11] = "";
        scanf("%s", word);
        bool check = true;
        int N = strlen(word);
        
        for (int i =0; i<N/2; i++){
        	if (word[i] != word[N-1-i]){
            	check = false;
		        break;
            }
        }
		printf("#%d %d\n", test_case, check);
	}
	return 0;
}

//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq
