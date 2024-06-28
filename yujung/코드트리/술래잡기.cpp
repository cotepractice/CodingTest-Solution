#include<iostream>
#include<vector>
using namespace std;
#define MAX_N 100
#define MAX_M 10000
#define MAX_K 101

struct s {
	int x, y, d;
};
s domang[MAX_M];//도망자 위치
int namu[MAX_N][MAX_N];
int n, m, h, k;

int sx;
int sy;
int sd;
int score[MAX_K];



int l = 0;
int cnt = 0;
int cl = 1;
bool flag = true;
int dx[4] = { 0,1,0,-1 };//1인 경우 좌우, 2인 경우 상하, 오,아
int dy[4] = { 1,0,-1,0 };//오른쪽,아래쪽
//3+2/4
//1+2/
//0+2
//2+2
int dx2[4] = { -1,0,1,0 };//위,오른.아래,왼
int dy2[4] = { 0,1,0,-1 };

bool is_range(int x, int y) {
	return 0 < x && 0 < y&&x <= n && y <= n;
}

void domang_move() {//도망자  m명 이동
	//술래와의 거리가 3 이하인 도망자만 움직
	for (int i = 1; i <= m; i++) {
		int x = domang[i].x;
		int y = domang[i].y;//도망자 위치
		int d = domang[i].d;
		if (x == -1 && y == -1)continue;//죽은 사람 못움직임
		if (abs(sx - x) + abs(sy - y) <= 3) {
			for (int k = 0; k < 2; k++) {
				int nx = x + dx[d];
				int ny = y + dy[d];



				if (is_range(nx, ny)) {//격자를 벗어나지 않는 경우
					if (nx == sx && ny == sy) {//움직이려는 칸에 술래가 있는 경우
						continue; //
					}
					else {//움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동
						domang[i] = { nx,ny,d };

						break;
					}
				}
				else {
					d = (d + 2) % 4;
				}
			}

		}
	}
	//현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우

	//	움직이려는 칸에 술래가 있는 경우라면 움직이지 않습니다.
	//	움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동합니다.해당 칸에 나무가 있어도 괜찮습니다.
	//	현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우

	//	먼저 방향을 반대로 틀어줍니다.이후 바라보고 있는 방향으로 1칸 움직인다 했을 때 해당 위치에 술래가 없다면 1칸 앞으로 이동합니다.
}




void sul_move() {
	int x = sx;
	int y = sy;
	int dir = sd;
	int nx = x + dx2[dir];
	int ny = y + dy2[dir];
	l++;
	if (l == cl) {
		l = 0;
		cnt++;
		if (flag) {//중앙부터
			if (dir == 3)dir = 0;
			else dir++;
		}
		else {//처음부터
			if (dir == 0)dir = 3;
			else dir--;
		}
		if (cnt == 2) {
			cnt = 0;
			if (flag) { cl++; }
			else { cl--; }
		}


	}
	if (nx == n / 2 + 1 && ny == n / 2 + 1) {
		flag = true;
		l = 0;
		cl = 1;
		cnt = 0;
		dir = 0;
	}
	if (nx == 1 && ny == 1) {
		flag = false;
		cnt = -1;
		dir = 2;
		l = 0;
		cl = n - 1;
	}

	sx = nx;
	sy = ny;
	sd = dir;
}


void japgi(int a) {
	int x = sx;
	int y = sy;
	int dir = sd;
	for (int i = 0; i < 3; i++) {
		int nx = x + dx2[dir] * i;
		int ny = y + dy2[dir] * i;
		if (!is_range(nx, ny))break;
		if (namu[nx][ny])continue;//나무 뒤에 있으면 못죽음

		for (int k = 1; k <= m; k++) {
			int cx = domang[k].x;
			int cy = domang[k].y;
			if (cx == -1 && cy == -1)continue; //이미 죽은거
			if (cx == nx && cy == ny) {

				domang[k].x = -1;
				domang[k].y = -1;

				score[a]++;//잡은 사람 수만큼증가
			}

		}
	}
}

bool check() {
	for (int i = 1; i <= m; i++) {
		int x = domang[i].x;
		int y = domang[i].y;
		if (!(x == -1 && y == -1))return false;
	}
	return true;
}
void input() {
	cin >> n >> m >> h >> k;//n은 홀수

	sx = n / 2 + 1;
	sy = n / 2 + 1;
	sd = 0;
	for (int i = 1; i <= m; i++) { //도망자의 위치, 1인 경우 좌우, 2인 경우 상하, 오,아
		int a, b, c;
		cin >> a >> b >> c;
		domang[i] = { a,b,c - 1 };

	}


	for (int i = 1; i <= h; i++) {
		int a, b;
		cin >> a >> b;
		namu[a][b] = 1;
	}
}
int main() {
	input();
	for (int i = 1; i <= k; i++) {
		domang_move();
		sul_move();
		japgi(i);
		if (check())break;
	}
	int sum = 0;
	for (int i = 1; i <= k; i++) {
		sum += i * score[i];
	}
	cout << sum;
}