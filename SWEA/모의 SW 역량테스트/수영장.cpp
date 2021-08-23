#include<iostream>
#include<algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int _day, _month, _3month, _year;
        int numb[12] = {0,};
        int pay[12] = {0, };
        cin >> _day >> _month >> _3month >> _year;
        
        for(int i=0; i<12; i++)
            cin >> numb[i];
        
        for(int i=0; i<12; i++){
            if(i==0) pay[0]=min(_day*numb[i], _month);
            else if(i < 3) pay[i]=min({pay[i-1]+_day*numb[i], pay[i-1]+_month, _3month});
            else pay[i] = min({pay[i-1]+_day*numb[i], pay[i-1]+_month, pay[i-3]+_3month});
        }
        
        printf("#%d %d\n", test_case, min(*max_element(pay, pay+12), _year));
        
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}

/*
algorithm 헤더 파일
숫자 대상 : min(숫자1, 숫자2), max(숫자1, 숫자2) -> 3개 이상일 경우 {숫자1, 숫자2, 숫자3, ...}안에 넣어주기
배열 대상 : min_element(ForwardIt first, ForwardIt last), max_element(ForwardIt first, ForwardIt last);


https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq
*/
