#include <string>
#include <vector>
#include<queue>
using namespace std;

char map[100][100];
int n;
int m;
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int sx,sy;
int lx,ly;
int ex,ey;
bool is_range(int x,int y){
    return x>=0&&y>=0&&x<n&&y<m;
}
int bfs(int x,int y,int ex,int ey){
    int cnt=0;
    bool visited[100][100]={false};
    queue<pair<int,pair<int,int>>> q;
    q.push({x,{y,cnt}});
    
    visited[x][y]=true;
    while(!q.empty()){
        auto a=q.front();
        q.pop();
        int cx=a.first;
        int cy=a.second.first;
        int ccount=a.second.second;
        if(cx==ex&&cy==ey){return ccount;}
        for(int i=0; i<4;i++){
            int nx=cx+dx[i];
            int ny=cy+dy[i];
            if(!is_range(nx,ny)||visited[nx][ny]==true||map[nx][ny]=='X'){
                continue;
            }
            
            q.push({nx,{ny,ccount+1}});
            visited[nx][ny]=true;
            
        }
    }
    return -1;
}
int solution(vector<string> maps) {
    int answer = 0;
     n=maps.size();
     m=maps[0].size();
    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
            map[i][j]=maps[i][j];
            if(map[i][j]=='S'){
                sx=i;
                sy=j;
            }else if(map[i][j]=='L'){
                lx=i;
                ly=j;
            }
            else if(map[i][j]=='E'){
                ex=i;
                ey=j;
            }
        }
    }
    
    int sum1=bfs(sx,sy,lx,ly);

    if(sum1==-1){
        return -1;
    }else{
        int sum2=bfs(lx,ly,ex,ey);
        if(sum2==-1){
            return -1;
        }else{
            return sum1+sum2;
        }
    }
  
}