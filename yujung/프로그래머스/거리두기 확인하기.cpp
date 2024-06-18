#include <string>
#include <vector>
#include<queue>
#include<cstring>

//vistied 초기화 위치 중요
using namespace std;
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int n,m;
  bool visited[5][5];
bool is_range(int x,int y){
    return (x>=0&&y>=0&&x<n&&y<m);
}
bool dfs(int x,int y,vector<string>  places){
    queue<pair<int,pair<int,int>>> q;
  //  bool visited[5][5]; 초기화를 원래 여기에 했었는데
    visited[x][y]=true;
    q.push({x,{y,0}});
    
    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second.first;
        int c=q.front().second.second;
        q.pop();
        if(c==2)continue;
         for(int i=0; i<4;i++){
        int nx=x+dx[i];
             int ny=y+dy[i];
             if(is_range(nx,ny)){
                 if(visited[nx][ny]==false){
                     if(places[nx][ny]=='O'){
                         visited[nx][ny]=true;
                         q.push({nx,{ny,c+1}});
                     }
                     else if(places[nx][ny]=='P')
                     {
                         return false;
                     }
                 }
             }
           
         }
    }
   return true;
}
vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    for(int i=0; i<places.size();i++){
        int f=1;
        n=places[i].size();
        m=places[i][0].size();
        memset(visited,false,sizeof(visited)); //이 위치에 초기화 하는 것이 중요
        for(int j=0; j<n;j++){
            for(int k=0; k<m;k++){
                if(places[i][j][k]=='P'){
                    if(dfs(j,k,places[i])==false){
                        answer.push_back(0);
                        f=0;
                        break;
                    };
                }
            }
            if(!f)break;
            
        }
        if(f){
                answer.push_back(1);
            }
        
    }
    return answer;
}