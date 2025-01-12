#include<iostream>
#include<vector>
#include<queue>
using namespace std;
#define MAX_N 100001
int ver, e;
vector<pair<int, int>> v[MAX_N];
bool visited[MAX_N];

priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
long long ans = 0;

int T = 0;

void prim() {
	pq.push({ 0, 1 });



	while (!pq.empty()) {
		int cost = pq.top().first;
		int cur_v = pq.top().second;
		pq.pop();

		if (visited[cur_v] == true)continue;
		visited[cur_v] = true;
		ans += cost;
		for (auto &edge : v[cur_v]) {
			int next_cost = edge.first;
			int next_v = edge.second;

			if (!visited[next_v]) {
				pq.push({ next_cost, next_v });
			}
		}
	}

}

void init() {
	ans = 0;
	for (int i = 1; i <= ver; i++) {
		visited[i] = false;
		v[i].clear();

	}
	while (!pq.empty()) pq.pop(); // 우선순위 큐 초기화
}
int main()
{

	cin >> T;

	for (int t = 1; t <= T; t++) {

		cin >> ver >> e;
		init();
		for (int i = 0; i < e; i++) {
			int a, b, c;
			cin >> a >> b >> c;
			v[a].push_back({ c,b });
			v[b].push_back({ c,a });
		}
		prim();
		cout << "#" << t << " " << ans << "\n";
	}


}