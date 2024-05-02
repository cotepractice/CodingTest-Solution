#include<iostream>
#include<cstring>
using namespace std;

int edge[11][11];
bool visited[11];
int ans;
int n, m;
void findLongPath(int idx, int cnt) {
	if (cnt > ans) {
		ans = cnt;
	}
	for (int i = 1; i <= n; i++) {
		if (edge[idx][i] && !visited[i]) { 
			visited[i] = true;
			findLongPath(i,cnt + 1);
			visited[i] = false;
		}
	}
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		memset(edge, 0, sizeof(edge));
		memset(visited, false, sizeof(visited));
		cin >> n >> m;
		for (int i = 0; i < m; i++) {
			int x, y;
			cin >> x >> y;
			edge[x][y] = 1;
			edge[y][x] = 1;
		}

		for (int i = 1; i <= n; i++) {
			visited[i] = true;
			findLongPath(i, 1);
			visited[i] = false;
		}
		cout << "#" << t << " " << ans << "\n";
	}
}