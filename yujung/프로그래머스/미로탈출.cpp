#include <string>
#include <vector>
#include <queue>
#include <cstring>
#include <iostream>

using namespace std;

pair<int, int> s = { -1,-1 };
pair<int, int> l = { -1,-1 };
pair<int, int> e = { -1,-1 };
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};


bool visited[101][101];
int bfs(vector<string>& maps,pair<int,int> src, pair<int,int> p) {
    


    queue<pair<int,pair< int,int>>> q;
    q.push({src.first,{src.second,0}});
    visited[src.first][src.second] = true;

    int n = maps.size();
    int m = maps[0].size();
    while (!q.empty()) {
        auto a = q.front();
        
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = a.first + dx[i];
            int ny = a.second.first + dy[i];
            if (nx==p.first&&ny==p.second) { return a.second.second+1; }
            if (!(nx >= 0 && ny >= 0 && nx < n && ny < m)) continue;
            if (maps[nx][ny] == 'X'||visited[nx][ny]==true) continue;
        
            visited[nx][ny]=true;
            q.push({ nx,{ny ,a.second.second+1} });
        }
    }
    return 0;
}

int solution(vector<string> maps) {
 

    int answer = 0;

    for (int i = 0; i < maps.size(); i++) {
        for (int j = 0; j < maps[0].size(); j++) {
            if (maps[i][j] == 'S') {
                s = { i,j };
            }
            else if (maps[i][j] == 'L') {
                l = { i,j };
            }
            else if (maps[i][j] == 'E') {
                e = { i,j };
            }
        }
    }
    memset(visited,false,sizeof(visited));
    
    int score = bfs(maps, s,l);
    if (!score) { return -1; }
    else {
        answer += score;
    }
  
    memset(visited,false,sizeof(visited));

   
    int score2=bfs(maps, l,e);
    
    if (!score2) { 
        return -1;
    }
    else {
        answer += score2;
    }
    
    return answer;
}
