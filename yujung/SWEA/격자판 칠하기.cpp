#include <iostream>
#include <string>
#include<queue>
#include<cstring>
using namespace std;


char map[50][50];
bool visited[50][50];
int dx[4] = { 0,0,1,-1 }; //오른쪽, 왼쪽 아래쪽, 위쪽
int dy[4] = { 1,-1,0,0 };
int n, m;
bool is_range(int x, int y) {
	return (x >= 0 && y >= 0 && x < n&&y < m);
}
bool bfs(int x,int y) {
	queue<pair<int, int>> q;
	q.push({ x,y });
	visited[x][y]=true;
	while (!q.empty()) {
		int x=q.front().first;
		int y = q.front().second;
		int cur_v = map[x][y];
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (!is_range(nx,ny)||visited[nx][ny]==true)continue;
			
			visited[nx][ny] = true;
			if (cur_v=='#'&&map[nx][ny]=='#') {
				return false;
			}
			else if (cur_v == '.'&&map[nx][ny] == '.') {
				return false;
			}
			else {
				if (cur_v == '#') {
					map[nx][ny] = '.';
					q.push({ nx,ny });
				}
				else if (cur_v == '.') {
					map[nx][ny] = '#';
					q.push({ nx,ny });
				}
			}

		}
	}
	return true;
}
int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> n >> m;

		memset(visited, false, sizeof(visited));

		int sx, sy;
		bool f = false;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> map[i][j];
				if (!f&&map[i][j] != '?') {//map은 있잖아
					sx = i;
					sy = j;
					f = true;
				}
			}
		}
		bool ans = bfs(sx, sy);
		if (ans == true) {
			cout << "#"<<t<<" "<<"possible"<<"\n";
		}
		else {
			cout << "#"<<t<<" "<<"impossible"<<"\n";
		}
	}
	
		

		
		
}