#include<iostream>
#define MAX_N 500
using namespace std;

int map[MAX_N][MAX_N];
int n;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { -1,0,1,0 };
int cr; //중앙점에서 시작할 수 있도록 초기화하지 않고 선언만 한다.
int cc;
int length = 1;
int cnt = 0;
int dir = 0;
int bigCnt = 0;

int rx[4][10] = { { -1,1,-1,1,-1,1,-2,2,0,0 },
				  { 0,0,1,1,2,2,1,1,3,2 },
				  { -1,1,-1,1,-1,1,-2,2,0,0 },
				  { 0,0,-1,-1,-2,-2,-1,-1,-3,-2 } };
int ry[4][10] = { { 0,0,-1,-1,-2,-2,-1,-1,-3,-2 },
				 { -1,1,-1,1,-1,1,-2,2,0,0 },
				 { 0,0,1,1,2,2,1,1,3,2 },
				 { -1,1,-1,1,-1,1,-2,2,0,0 } };

int percent[] = { 1,1,7,7,10,10,2,2,5 };

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < n;
}

int ans = 0;

void move(int sx, int sy, int ex, int ey, int dir) {
	int mo = map[ex][ey];
	map[ex][ey] = 0;
	int sum = mo;
	for (int i = 0; i < 9; i++) {
		int nx = sx + rx[dir][i];
		int ny = sy + ry[dir][i];
		int spread = mo * (0.01 * percent[i]);
		sum -= spread;
		if (is_range(nx, ny)) {
			map[nx][ny] += spread;
		}
		else {
			ans += spread;
		}
	}
	int nx = sx + rx[dir][9];
	int ny = sy + ry[dir][9];
	if (is_range(nx, ny)) {
		map[nx][ny] += sum;
	}
	else {
		ans += sum;
	}
}

void tornado() {
	cr = n / 2;
	cc = n / 2;
	while (1) {
		if (dir >= 4) {
			dir = 0;
		}
		int nx = cr + dx[dir];
		int ny = cc + dy[dir];
		if (!is_range(nx, ny)) break;

		if (map[nx][ny] > 0) {
			move(cr, cc, nx, ny, dir);
		}

		cnt++;

		if (length == cnt) {
			cnt = 0;
			dir++;
			bigCnt++;
		}

		if (bigCnt == 2) {
			length++;
			bigCnt = 0;
		}
		cr = nx;
		cc = ny;
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}

	int sum1 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			sum1 += map[i][j];
		}
	}
	tornado();
	int sum2 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			sum2 += map[i][j];
		}
	}
	cout << sum1 - sum2  << "\n"; // 바깥으로 나간 모래의 양을 합산하여 출력
}