#include <string>
#include <vector>
#include<queue>
using namespace std;

char map[100][100];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int sx,sy;
int n,m;
bool visited[100][100];
bool is_range(int x,int y){
    return 0<=x&&x<n&&0<=y&&y<m;
}

bool check_D(int x,int y){
    if(map[x][y]=='D'){
        return true;
    }else{
        return false;
    }
}

int bfs(){
    int cnt=0;
    queue<pair<int,pair<int,int>>> q;
    q.push({sx,{sy,cnt}});
    visited[sx][sy]=true;
    while(!q.empty()){
        pair<int,pair<int,int>> c=q.front();
        q.pop();
        
      
        if(map[c.first][c.second.first]=='G'){return c.second.second;}
       
        
        for(int i=0; i<4;i++){
              int nx=c.first+dx[i];
            int ny=c.second.first+dy[i];
              
            while(is_range(nx,ny)&&!check_D(nx,ny)){
                nx+=dx[i];
                ny+=dy[i];
            }
              nx-=dx[i];
              ny-=dy[i];
            
            
             if (!visited[nx][ny]) {
                visited[nx][ny] = true;
                q.push({nx, {ny, c.second.second+1}});
            }
        }
    }
                        return -1;
}
int solution(vector<string> board) {
    int answer = 0;
    n=board.size();
    m=board[0].size();
    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
            map[i][j]=board[i][j];
            
            if(board[i][j]=='R'){
            sx=i;
            sy=j;
        }
        }
        
    }
    answer=bfs();
    return answer;
}