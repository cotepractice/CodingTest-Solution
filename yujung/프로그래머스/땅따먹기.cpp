
#include <vector>
#include<algorithm>
using namespace std;


//bfs로 풀었을때 안되면 dp로



int solution(vector<vector<int> > land)
{
    
    int answer=0;
    int n=land.size();
    int dp[1000001][4];
    for(int i=0;i<4;i++) dp[0][i]=land[0][i];
    for(int i=1; i<n;i++){
        for(int j=0; j<4;j++){
            int tmp=0;
            for(int k=0;k<4;k++){
                if(j==k)continue;
                tmp=max(tmp,dp[i-1][k]);
            }
              dp[i][j]=tmp+land[i][j];
        }
      
    }
    

        for(int j=0; j<4;j++){
            answer=max(answer,dp[n-1][j]);
        }
      
    return answer;
}