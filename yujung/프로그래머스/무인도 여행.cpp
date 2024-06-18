#include <string>
#include <vector>
#include<queue>
#include<algorithm>
using namespace std;
    
    queue<pair<int,int>> q;
int dx[4]={0,0,1,-1};
    int dy[4]={1,-1,0,0};

int cnt=0;
void bfs(vector<string> &arr){

    int n=arr.size();
    int m=arr[0].size();
    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();
        for(int i=0;i<4;i++){
            int nx=x+dx[i];
        int ny=y+dy[i];
            if(!(nx>=0&&ny>=0&&nx<n&&ny<m))continue;
            if(arr[nx][ny]-'0'<10){
                cnt+=arr[nx][ny]-'0';
                q.push({nx,ny});
                arr[nx][ny]='X';
            }
        }
    }
}
vector<int> solution(vector<string> maps) {
    vector<int> answer;
    int n=maps.size();
 int m=maps[0].size();
    
    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
           if(maps[i][j]-'0'<10){//숫자라면
               cnt=maps[i][j]-'0';
               maps[i][j]='X';
               q.push({i,j});
               bfs(maps);
               answer.push_back(cnt);
           }
        }
    }
    if(answer.size()>0){
        sort(answer.begin(),answer.end());
    }else{
        answer.push_back(-1);
    }
 
    return answer;
}