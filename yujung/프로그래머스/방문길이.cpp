#include <string>
#include<map>
using namespace std;

map<char,int> m;
int dx[4]={0,0,1,-1}; //오,왼,아래,위
int dy[4]={1,-1,0,0}; 
    int answer = 0;
int arr[11][11][11][11];
  int x=5;
    int y=5;

void func(char dir){
  int nx=x+dx[m[dir]];
  int ny=y+dy[m[dir]];
 if(!(nx>=0&&ny>=0&&nx<=10&&ny<=10))return;
 if(arr[x][y][nx][ny]==0&&arr[nx][ny][x][y]==0){
     arr[x][y][nx][ny]=1;
     arr[nx][ny][x][y]=1;
     answer++;
  
 }
       x=nx;
     y=ny;
    
}
int solution(string dirs) {

    m['R']=0;
    m['L']=1;
    m['D']=2;
    m['U']=3;
  //  arr[5][5]=1;
    for(int i=0; i<dirs.size();i++){
        func(dirs[i]);
    }
    return answer;
}