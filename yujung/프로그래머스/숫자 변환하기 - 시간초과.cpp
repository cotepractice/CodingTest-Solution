#include <string>
#include <vector>
#include<cstring>
#include<cmath>
int answer=1000000;

//x에 n을 
bool visited[1000001];
void dfs(int x,int y,int n,int cnt){

    if(x>y){
        return;
    }
   if(x==y){
       answer=fmin(cnt,answer);
   } 
    

    dfs(x+n,y,n,cnt+1);
 
    dfs(x*2,y,n,cnt+1);

    dfs(x*3,y,n,cnt+1);

  
}

using namespace std;

int solution(int x, int y, int n) {
    
    memset(visited,false,sizeof(visited));
    dfs( x, y, n,0);
    if(answer==1000000){
        answer=-1;
    }
    return answer;
}