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

queue < pair<int, int>> q;
queue < pair<int, int>> q1;
queue < pair<int, int>> b;
queue < pair<int, int>> c;
bool ch[1501][1501];

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < m;
}
bool check() {
	
	
	b.push({ startx,starty });
	ch[startx][starty] = true;
	while (!b.empty()) {
		pair<int, int> a = b.front();
	
		b.pop();
		for (int i = 0; i < 4; i++) {
			int nx = a.first + dx[i];
			int ny = a.second + dy[i];
			if (!is_range(nx, ny)|| ch[nx][ny])continue;
			ch[nx][ny] = true; //방문

			if (arr[nx][ny] == 'X') { 
				c.push({ nx,ny });
				 }
			else if (arr[nx][ny] == '.') b.push({ nx,ny });
			else if (arr[nx][ny] == 'L') {
				return true;
			
			}
		}
	}
	return false;
}

void play() {

	while (!q.empty()) {
		pair<int, int> a = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = a.first + dx[i];
			int ny = a.second + dy[i];
			if (!is_range(nx, ny))continue;
			if (arr[nx][ny] == '.') continue;
			if (arr[nx][ny] == 'X') {
				arr[nx][ny] = '.';
				q1.push({ nx,ny });
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	bool flag = false;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
			if (flag == false && arr[i][j] == 'L') {
				startx = i;
				starty = j;
				flag = true;
			}
			else if (flag == true && arr[i][j] == 'L') {
				endx = i;
				endy = j;
			}
			if (arr[i][j] !='X') {
				q.push({ i,j });
			}
			
		}
	}


	int cnt = 0;
	while (1) {
		if (check()) { break; }
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << ch[i][j];
			}
			cout << "\n";
		}
		b = c;
		play();
		q = q1;
		cnt++;
		while (!c.empty())c.pop();
		while (!q1.empty())q1.pop();

	}
	cout << cnt;

}