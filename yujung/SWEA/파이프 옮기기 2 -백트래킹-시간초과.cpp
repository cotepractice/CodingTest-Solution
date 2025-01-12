#include<iostream>
using namespace std;
#define MAX_N 32

int n;
int dx[3] = { 0,1,1 };
int dy[3] = { 1,1,0 };
int map[MAX_N][MAX_N];
int cnt = 0;

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < n;
}
void dfs(int cur, int x, int y)
{
	if (x == n - 1 && y == n - 1) {
		cnt++;
		return;
	}
	for (int i = 0; i < 3; i++)
	{
		if (cur == 0) {
			if (i == 2)continue;
		}
		if (cur == 2)
		{
			if (i == 0)continue;
		}

		int nx = x + dx[i];
		int ny = y + dy[i];
		if (!is_range(nx, ny))continue;
		if (map[nx][ny] == 1)continue;
		if (i == 1 && (map[x + 1][y] == 1 || map[x][y + 1] == 1)) continue;
		dfs(i, nx, ny);
	}

}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> map[i][j];
		}
	}
	dfs(0, 0, 1);

	cout << cnt;

}