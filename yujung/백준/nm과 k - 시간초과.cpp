#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
#define MAX_N 10


int n, m, k;
int map[MAX_N][MAX_N];
int tmp[MAX_N][MAX_N];
int t;
vector<int> v;
int res=-100000000;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < m;
}
bool check(vector<int> v) {
	memset(tmp, 0, sizeof(tmp));
	for (int i = 0; i < v.size(); i++) {
		int row = v[i] / m;
		int col = v[i] % m;
		tmp[row][col]=1;
	}
	int f = true;
	for (int i = 0; i < v.size(); i++) {
		int row = v[i] / m;
		int col = v[i] % m;
		
		for (int j = 0; j < 4; j++) {
			int nx = row + dx[j];
			int ny = col + dy[j];
			if (!is_range(nx, ny))continue;
			if (tmp[nx][ny] == 1) {
				return false;
			}
		}
	}
	return true;
}
void dfs(int cnt, int idx) {
	if (cnt ==k )
	{
		int f=check( v);
		if (f == true) {
			int cur = 0;
			for (int i = 0; i < v.size(); i++) {
				int row = v[i] / m;
				int col = v[i] % m;
				cur += map[row][col];
			}
			if (res < cur) {
				res = cur;
			}
			
		}
	}

	for (int i = idx; i < t; i++) {
		v.push_back(i);
		dfs(cnt + 1, i+1);
		v.pop_back();
	}
}

int main() {
	cin >> n >> m >> k;
	t = n * m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	dfs(0, 0);

	cout << res;


}