#include <string>
#include <vector>
#include <memory.h>

using namespace std;

int map[2][200001];
int dp[200001];

int solution(int n, vector<int> tops){
    int answer = 0;
    memset(map, -1, sizeof(map));
   
    for(int i=0; i<n; i++) map[0][2*i+1] = tops[i];  //2층(뿔)
    for(int i=0; i<2*n+1; i++) map[1][i] = 1;		//1층
    
    dp[0] = 1;						//n=0일때는 1가지
    if(map[0][1] == 1) dp[1] = 3;	//n=1일 때 뿔이 있으면 3가지
    else dp[1] = 2;					//뿔이 없으면 2가지

    for(int i=2; i<2*n+1; i++){
        if(i%2 == 0){				//짝수
            dp[i] = dp[i-1] + dp[i-2];
        }
        else{						//홀수
            if(map[0][i] == 1) dp[i] = 2*dp[i-1] + dp[i-2];	//뿔이 있는 경우
            else dp[i] = dp[i-1] + dp[i-2];					//뿔이 없는 경우
        }
        dp[i] %= 10007;				//매번 1007로 나눈 나머지를 대입
    }

    return dp[2*n];					//2n+1번째의 경우의 수 출력
}