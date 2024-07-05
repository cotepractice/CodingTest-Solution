#include <string>
#include <vector>
#include<queue>
#include<cstring>
#include<set>
#define MAX_N 501
using namespace std;

int n,m;
int res[MAX_N];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
 int answer = 0;
int max_v=-1;
set<int> s;
bool is_range(int x,int y){
    return x>=0&&y>=0&&x<n&&y<m;
}
int bfs(int x, int y,vector<vector<int>> &land){
    land[x][y]=0;
    queue<pair<int,int>> q;
    q.push({x,y});
    s.insert(y);
    int cnt=1;
    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();
        for(int i=0;i<4;i++){
            int nx=x+dx[i];
            int ny=y+dy[i];
            if(!is_range(nx,ny))continue;
            if(land[nx][ny]==0)continue;
            land[nx][ny]=0;
            q.push({nx,ny});
            s.insert(ny);
            cnt++;
        }
    }
    return cnt;
}

void check(vector<vector<int>> land){
    for(int i=0; i<m;i++){
        for(int j=0; j<n;j++){
            if(land[j][i]==1){
                int cur=bfs(j,i,land);
                for(auto a: s){
                    res[a]+=cur;
                }
                s.clear();
            }
        }
       
      
    }
    
}
int solution(vector<vector<int>> land) {
   
    n=land.size();
    m=land[0].size();
    check(land);
    for(int i=0; i<m;i++){
        int cur=res[i];
          if(max_v<cur){
              max_v=cur;
          }  
    }

    answer=max_v;
    return answer;
}