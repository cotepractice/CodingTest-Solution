#include<iostream>
using namespace std;
#define MAX_N 20
#define MAX_M 20
int N, M;//지도의 세로 가로

int K;//명령의 개수

int map[MAX_N][MAX_M];
//동서북남
int dx[5] = { 0,0,0,-1,1 };
int dy[5] = { 0,1,-1,0,0 };
int dice[6] = { 0,0,0,0,0,0 };//아래,위,북,동,남,서
int tmp[6] = { 0,0,0,0,0,0 };
int x = 0;
int y = 0;
bool is_range(int x, int y) {
	if (x >= 0 && y >= 0 && x < N && y < M)return true;
	return false;
}
void copy() {
	for (int i = 0; i < 6; i++) {
		tmp[i] = dice[i];
	}
}
void dice_play(int dir) {
	copy();
	//아래0, 위1, 북2, 동3, 남4, 서5
	if (dir == 1) {
		dice[3] = tmp[1];
		dice[0] = tmp[3];
		dice[5] = tmp[0];
		dice[1] = tmp[5];
	}
	if (dir == 2) {
		dice[1] = tmp[3];
		dice[5] = tmp[1];
		dice[0] = tmp[5];
		dice[3] = tmp[0];
	}
	if (dir == 4) {
		dice[4] = tmp[1];
		dice[0] = tmp[4];
		dice[2] = tmp[0];
		dice[1] = tmp[2];
	}
	if (dir == 3) {
		dice[2] = tmp[1];
		dice[0] = tmp[2];
		dice[4] = tmp[0];
		dice[1] = tmp[4];
	}
}
void play(int dir) {
	int nx = x + dx[dir];
	int ny = y + dy[dir];
	if (!is_range(nx, ny))return;
	dice_play(dir);
	cout << dice[1] << "\n";
	if (map[nx][ny] == 0) {
		map[nx][ny] = dice[0];
	}
	else {
		dice[0] = map[nx][ny];
		map[nx][ny] = 0;
	}
	x = nx;
	y = ny;
	//cout << "test"<<x << y;

}
int main() {
	cin >> N >> M;
	cin >> x >> y;
	cin >> K;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}

	for (int i = 0; i < K; i++) {
		int a;
		cin >> a;
		play(a);
		//명령실행
	}
	
	//0 2
	// 3 4
	//

}