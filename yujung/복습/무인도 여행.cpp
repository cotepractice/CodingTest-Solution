#include <string>
#include <vector>
#include<queue>
#include<algorithm>
using namespace std;
#define MAX_N 101

bool visited[MAX_N][MAX_N];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
   int n;
    int m;
bool is_range(int x,int y){
    return x>=0&&y>=0&&x<n&&y<m;
}
int bfs(int x,int y,vector<string> & maps){
    queue<pair<int,int>> q;
    visited[x][y]=true;
    q.push({x,y});
    int sum=maps[x][y]-'0';
    
    while(!q.empty()){
        int cx=q.front().first;
        int cy=q.front().second;
       q.pop();
        for(int i=0; i<4;i++){
             int nx=cx+dx[i];
             int ny=cy+dy[i];
           
             if (!is_range(nx, ny) || maps[nx][ny] == 'X' || visited[nx][ny]) {
                continue;
            }
            q.push({nx,ny});
            visited[nx][ny]=true;
            sum+=maps[nx][ny]-'0';
        }
    }
    return sum;
}
vector<int> solution(vector<string> maps) {
    vector<int> answer;
   n=maps.size();
    m=maps[0].size();
    
    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
            if(visited[i][j]==false&&maps[i][j]!='X'){
              int a=bfs(i,j,maps);
                answer.push_back(a);
            }
        }
    }
    if(answer.size()==0){
        answer.push_back(-1);
    }else{
            sort(answer.begin(),answer.end());
    }

    return answer;
}