#include <string>
#include <vector>
#include<map>
using namespace std;
//다섯 광물을 캐고 철 곡괭이로 남은 다이아몬드, 철, 돌 1개
//더 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지
vector<pair<int,int>> v;
int board[3][3]={{1,1,1},{5,1,1},{25,5,1}};
map<string,int> m;
int min_v=25*50+1;
void dfs(vector<int> picks,vector<string> & minerals,int sum,int j){
    if(j==minerals.size()||(picks[0]==0&&picks[1]==0&&picks[2]==0)){
        if(min_v>sum){
            min_v=sum;
        }
        return;
    }
    for(int i=0; i<3;i++){
        if(picks[i]!=0){
            picks[i]--;
            int tmp=sum;
            int k;
            for(k=j;k<j+5&&k<minerals.size();k++){
                tmp+=board[i][m[minerals[k]]];
            }
            dfs(picks, minerals,tmp,k);
            picks[i]++;
        }
      
    }
}
int solution(vector<int> picks, vector<string> minerals) {
    int answer = 0;
    m["diamond"]=0;
    m["iron"]=1;
    m["stone"]=2;
   dfs( picks,minerals,0,0);
   
    return min_v;
}