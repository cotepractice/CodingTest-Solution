#include <string>
#include <vector>
#include<queue>
//n개의 노드가 있는 그래프가 잇습니다. 각
using namespace std;
vector<int> v[20001];
int cnt[20001];

int visited[20001];
void bfs(int n){
    
    queue<int> q;
    
    q.push(n);
    visited[n]=true;
    cnt[n]=0;
   while(!q.empty()){
       int a=q.front();
       q.pop();
       for(int i=0; i<v[a].size();i++){
           if(visited[v[a][i]]==true)continue;
           visited[v[a][i]]=true;
           cnt[v[a][i]]=cnt[a]+1;
           q.push(v[a][i]);
       }
      
       }
}
int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    for(int i=0; i<edge.size();i++){
        v[edge[i][0]].push_back(edge[i][1]);
        v[edge[i][1]].push_back(edge[i][0]);
    }
    bfs(1);
    
    int max_n=0;
    for(int i=1; i<=n;i++){
        if(max_n<cnt[i]){
            max_n=cnt[i];
        }
    }
    
    for(int i=1; i<=n;i++){
        if(max_n==cnt[i]){
            answer++;
        }
    }
    return answer;
}