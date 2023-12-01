//다익스트라-최단경로
#include<iostream>
#include<queue>
#include<vector>
#define endl "\n"
#define  MAX 20010
#define INF 987654321
using namespace std;

int v, e, start;
int dist[MAX];
vector<pair<int, int>> vertex[MAX];

void dijkstra() {
	priority_queue<pair<int, int>> pq;
	pq.push(make_pair(0, start));
	dist[start] = 0;
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int cur = pq.top().second;
		pq.pop();
		for (int i = 0; i < vertex[cur].size(); i++) {
			int next = vertex[cur][i].first;
			int nCost = vertex[cur][i].second;
			if (dist[next] > cost + nCost)
			{
				dist[next] = cost + nCost;
				pq.push(make_pair(-dist[next], next));

			}
		}
	}
	for (int i = 1; i <= v; i++) {
		if (dist[i] == INF)cout << "INF" << endl;
		else cout << dist[i] << endl;
	}

}
int main() {
	cin >> v >> e >> start;
	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		vertex[a].push_back(make_pair(b, c));
	}
	for (int i = 1; i <= v; i++) {
		dist[i] = INF;
	}
	dijkstra();

	
}