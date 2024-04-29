#include <iostream>
#include <string>
#include <queue>

using namespace std;

char map[20][20];

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int n;
bool is_range(int x,int y) {
	return x >= 0 && y >= 0 && x < n&&y < n;
}
int bfs(int x,int y) {
	queue<pair<int,int>> q;
	int visited[20][20];
	q.push({ x,y });
	visited[x][y] = true;
	int cnt = 1;
	while (!q.empty()) {
		int x=q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(!is_range(nx,ny)||visited[nx][ny]==true)continue;
			visited[nx][ny] = true;
			if (map[nx][ny] == '#') {
				cnt++;
				q.push({ nx,ny });
			}
		}
	}
	return cnt;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string ans = "yes";
	cin >> n;
	int cnt = 0;
	bool f = false;
	int real_cnt = 0;
	int sx, sy;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < n; j++) {
			map[i][j]=s[j];
			if (map[i][j] == '#')cnt++;
			if (map[i][j] == '#'&&f==false) {
				f = true;
			
				sx = i;
				sy = j;
			}
		}
	}
	real_cnt = bfs(sx,sy);
	cout << real_cnt << cnt;
	if (cnt != real_cnt) {
		
		ans = "no";
	}
	
	else {

		int h = 0;
		for (int i = sy; i <= n; i++) {
			
			if (map[sx][i] != '#') { break; }
			h++;
		}
		int w = 0;
		for (int i = sx; i <= n; i++) {
			if (map[i][sy] != '#') { break; }
			w++;
		}
		if (h != w)ans = "no";
		if (h*w != cnt) ans = "no"; //사각형에 빈칸이 있는지 확인
	}
	
		cout << "#" << t << " " << ans << "\n";
	}

	
}