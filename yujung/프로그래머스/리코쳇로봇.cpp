#include <string>
#include <vector>
#include<queue>
using namespace std;
pair<int,int> r;
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int visited[100][100];
int n,m;
int dfs(vector<string> board){
    queue<pair<int,int>> q;
    q.push({r.first,r.second});
    visited[r.first][r.second]=1;
    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();
        for(int i=0; i<4;i++){
            int nx=x;
            int ny=y;
            while(1){
                nx+=dx[i];
                ny+=dy[i];
                
                if(!(nx>=0&&ny>=0&&nx<n&&ny<m)||board[nx][ny]=='D'){
                    nx-=dx[i];
                    ny-=dy[i];
                    break;
                }
                
            }
            if(visited[nx][ny]!=0){
                    continue;
                }
              
                visited[nx][ny]=visited[x][y]+1;
                q.push({nx,ny});
            if(board[nx][ny]=='G'){
                    return visited[nx][ny];
                }
              
        }
    }
    return 0;
}
int solution(vector<string> board) {
    int answer = 0;
    n=board.size();
    m=board[0].size();
    for(int i=0; i<board.size();i++){
        for(int j=0; j<board[0].size();j++){
            if(board[i][j]=='R'){
                r={i,j};
            }
        }
    }
    answer=dfs( board)-1;
    return answer;
}