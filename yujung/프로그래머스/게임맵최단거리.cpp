#include<vector>
#include<queue>
using namespace std;

int map[101][101];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int visited[101][101];
queue<pair<int,int>> q;

bool isRange(int x,int y, int r, int c){ 
    if(x<r&&x>=0&&y<c&&y>=0){
        return true;
    }
    return false;
}
void bfs(int r,int c){
   
    q.push({0,0});
    visited[0][0]=true;
    while(!q.empty()){
        pair<int,int> tmp=q.front();
        q.pop();
        for(int i=0; i<4;i++){
            int nx=tmp.first+dx[i];
            int ny=tmp.second+dy[i];
            if(map[nx][ny]!=0&&visited[nx][ny]==false&&isRange(nx,ny,r,c)) {
            visited[nx][ny]=true;
                map[nx][ny]=map[tmp.first][tmp.second]+1;
                q.push({nx,ny});
            }
    }
}
}
int solution(vector<vector<int> > maps)
{
    int answer = 0;
    for(int i=0; i<maps.size(); i++){
        for(int j=0; j<maps[0].size();j++){
            map[i][j]=maps[i][j];
        }
    }
    bfs(maps.size(),maps[0].size());
    
    if(map[maps.size()-1][maps[0].size()-1]==1){
        return -1;
    }else{
            return map[maps.size()-1][maps[0].size()-1];
    }

}