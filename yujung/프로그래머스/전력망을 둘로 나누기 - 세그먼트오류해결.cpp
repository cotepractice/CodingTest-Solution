#include <string>
#include <vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include <cstring> // memset 함수를 사용하기 위해 추가
using namespace std;
#define MAX_N 101 //범위 수정

vector<int> info[MAX_N];

int cnt=1;

void bfs(int a, int b){
 //   cnt=1;
    queue<int> q;
    bool visited[MAX_N];
    memset(visited, false, sizeof(visited)); // visited 배열 초기화
   // vector<bool> visited(MAX_N);
    q.push(a);
    visited[a]=true;
    visited[b]=true;
    while(!q.empty()){
        int v1=q.front();
        q.pop();
        
        for(int i=0; i<info[v1].size();i++){
              int v2=info[v1][i];
            if(visited[v2]==true)continue;
          cnt++;
            q.push(v2);
            visited[v2]=true;
            
        }
        
        
    }
}
int solution(int n, vector<vector<int>> wires) {
    int answer = 100;
    for(int i=0; i<wires.size();i++){
    int node1 = wires[i][0];
    int node2 = wires[i][1];
    info[node1].push_back(node2);
    info[node2].push_back(node1); // 두 노드를 서로 연결하는 간선 추가
    }
    for(int i=0; i<wires.size();i++){
        
        cnt=1;
        int a=wires[i][0];
        int b=wires[i][1];
        bfs(a,b);
        
        answer=min(answer,abs(2*cnt-n));
    }
    
    return answer;
}