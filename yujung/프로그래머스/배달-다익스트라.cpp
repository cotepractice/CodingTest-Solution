#include <iostream>
#include <vector>
#include<queue>
using namespace std;

vector<int> dist;
vector<pair<int,int>> v[51];
void dijkstra(){
    priority_queue<pair<int,int>> pq;
    pq.push({0,1});
    dist[1]=0;
    while(!pq.empty()){
        int cost=-pq.top().first;
        int ver=pq.top().second;
        pq.pop();
        for(int i=0; i<v[ver].size();i++){
            int ncost=v[ver][i].first;
            int nver=v[ver][i].second;
            if(dist[nver]>cost+ncost){
                dist[nver]=cost+ncost;
                pq.push({-dist[nver],nver});
            }
        }
    }
}
int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    dist.resize(N+1,2e9);

    for(int i=0; i<road.size();i++){
        int a=road[i][0];
        int b=road[i][1];
        int c=road[i][2];
        v[a].push_back({c,b});
        v[b].push_back({c,a});
    }
    dijkstra();
    for(int i=1;i<=N;i++){
        if(dist[i]<=K) answer++;
    }
    return answer;
}