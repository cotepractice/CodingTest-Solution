#include<iostream>
#include<queue>
#include<string>
using namespace std;
#define MAX_N 101
int n, m;

int map[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0};
queue<pair<int, int>> q;
bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < m;
}
void bfs(int sx, int sy ) {
	q.push({ sx,sy });
	visited[sx][sy] = true;

	while (!q.empty())
	{
		int cx = q.front().first;
		int cy = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			if (!is_range(nx, ny) || visited[nx][ny] || map[nx][ny] == 0)continue;
			q.push({ nx,ny });
			map[nx][ny] = map[cx][cy] + 1;
			visited[nx][ny] = true;
		}
	}
}
int main() {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < m; j++) {
			map[i][j]=s[j]-'0';
		}
	}

	bfs(0, 0);
	cout << map[n - 1][m - 1];
}