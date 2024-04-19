#include <string>
#include <vector>

using namespace std;

int visited[8];
int answer=0;
void dfs(int k, int cnt,vector<vector<int>> dungeons){

      answer=max(cnt, answer);
  
    for(int i=0; i<dungeons.size();i++){
        if(visited[i]==true)continue;
        if(k<dungeons[i][0])continue;
        visited[i]=true;
        dfs(k-dungeons[i][1],cnt+1,dungeons);
        visited[i]=false;
    }
          
}
int solution(int k, vector<vector<int>> dungeons) {
  
    dfs(k,0,dungeons);
    return answer;
}
