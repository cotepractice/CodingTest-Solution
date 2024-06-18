#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
#define MAX_N 100002
using namespace std;

int n, m;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
char arr[1500][1500];
int startx, starty;
int endx, endy;
int tmp[1500][1500];

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < m;
}
bool check() {
	memset(tmp, 0, sizeof(tmp));
	queue < pair<int, int>> q;
	q.push({ startx,starty });
	tmp[startx][starty] = 1;
	while (!q.empty()) {
		pair<int, int> a = q.front();
		if (a.first == endx && a.second == endy)return true;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = a.first + dx[i];
			int ny = a.second + dy[i];
			if (!is_range(nx, ny))continue;
			if (tmp[nx][ny] !=0||arr[nx][ny]=='X') continue;
			
			tmp[nx][ny] += tmp[a.first][a.second];
			q.push({ nx,ny });
		}
	}
	return false;
}

void play() {
	queue < pair<int, int>> q;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] == '.') {
				q.push({ i,j });
			}
		}
	}

	while (!q.empty()) {
		pair<int,int> a=q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = a.first + dx[i];
			int ny = a.second + dy[i];
			if (!is_range(nx, ny))continue;
			if (arr[nx][ny] == '.') continue;
			if (arr[nx][ny] == 'X') {
				arr[nx][ny] = '.';
			}
		}
	}
}
int main() {
	bool flag = false;
	cin >> n>>m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
			if (flag==false&&arr[i][j] == 'L') {
				startx = i;
				starty = j;
				flag = true;
			}
			else if (flag == true && arr[i][j] == 'L') {
				endx = i;
				endy = j;
			}
		}
	}
	
	
	
	int cnt = 0;
	while (1) {
		if (check()) { break; }
		play();
		cnt++;
	}
	cout << cnt;

}