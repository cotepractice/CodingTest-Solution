#include <string>
#include <vector>
#include<queue>
using namespace std;

priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
vector<pair<int,int>> v[101];
int visited[101];
int sum=0;
void prim(int a){
    visited[a]=true;
    for(int i=0; i<v[a].size();i++){
        if(!visited[v[a][i].second]){
            pq.push({v[a][i].first,v[a][i].second});
        }
    }
    while(!pq.empty()){
        pair<int, int> pp=pq.top();
        pq.pop();
        if(!visited[pp.second]){
            sum+=pp.first;
            prim(pp.second);
        }
    }
}
int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    for(int i=0; i< costs.size(); i++){
        v[costs[i][0]].push_back({costs[i][2],costs[i][1]});
        v[costs[i][1]].push_back({costs[i][2],costs[i][0]});
    }
    prim(0);
    return sum;
}