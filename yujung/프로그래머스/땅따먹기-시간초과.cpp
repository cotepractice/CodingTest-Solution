#include <iostream>
#include <vector>
using namespace std;
//땅따먹기 게임을 하려고 땅따먹기 게임의 땅은 총 N행 4열로
//모든 칸에는 점수가 쓰여. 1행부터 땅 밟으며 한행씩
//16점이 최고점이 되므로 16
int n;
int answer=0;

    
    
void dfs(int cnt,int cur,int sum,vector<vector<int> > land){
    if(cnt==n){answer=max(sum,answer);return;}
    for(int i=0; i<4;i++){
        if(cur==i)continue;
     
          dfs(cnt+1, i,sum+land[cnt][i],land);
    }
  
}
int solution(vector<vector<int> > land)
{

    n=land.size();
     dfs(0,-1,0,land);


    return answer;
}