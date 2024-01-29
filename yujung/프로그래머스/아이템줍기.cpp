#include <string>
#include <vector>
#include<queue>
using namespace std;

queue<pair<int,int>> q;
int map[110][110]={0};
int visited[102][102]={0};

int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};


int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
     for(int i=0;i<rectangle.size();i++){
         
        for(int j=0;j<rectangle[0].size();j++){
        rectangle[i][j]*=2;
        }
          int x1=rectangle[i][0];
          int y1=rectangle[i][1];
          int x2=rectangle[i][2];
          int y2=rectangle[i][3];
         
         for(int y=y1;y<=y2;y++){
             for(int x=x1;x<=x2;x++){
                 map[y][x]=1;
             }
         }   
     }
    
    
      for(int i=0;i<rectangle.size();i++){
          
          int x1=rectangle[i][0];
          int y1=rectangle[i][1];
          int x2=rectangle[i][2];
          int y2=rectangle[i][3];
          
          for(int y=y1+1;y<y2;y++){
             for(int x=x1+1;x<x2;x++){
                 map[y][x]=0;
             }
         }  
      }
    characterX*=2;
    characterY*=2;
    itemX*=2;
    itemY*=2;
    
    q.push({characterX,characterY});
    while(!q.empty()){
        int cx=q.front().first;
        int cy=q.front().second;
        q.pop();
        if(cy==itemY&&cx==itemX)
            break;
        for(int i=0; i<4; i++){
            int nx=cx+dx[i];
            int ny=cy+dy[i];
           if(map[ny][nx]==1)
           {
               q.push({nx,ny});
               map[ny][nx]=map[cy][cx]+1;
           }
        }
    }
     int answer = 0;
     answer=map[itemY][itemX]/2;
    return answer;
}