#include <string>
#include <vector>

using namespace std;
int visited[200];

void dfs(int i, int n, vector<vector<int>> computers){
    visited[i]=true;
    for(int j=0; j<n;j++){
        if(visited[j]==false&&computers[i][j]==1){
            dfs(j,n,computers);
        }
    }
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for(int i=0;i<n;i++){
        if(visited[i]==false){
            dfs(i,n, computers);
            answer++;
        }
    }
    return answer;
}