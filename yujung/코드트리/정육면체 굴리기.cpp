#include<iostream>
#define MAX_N 20
#define MAX_K 1000
using namespace std;

int n, m, x, y, k;
int dx[5] = { 0, 0, 0, -1, 1 }; // 동, 서, 북, 남
int dy[5] = { 0, 1, -1, 0, 0 };
int map[MAX_N][MAX_N];
// 주사위 각 면의 값 (1: 위, 6: 아래, 2: 앞, 5: 뒤, 3: 오른쪽, 4: 왼쪽)
int dir[MAX_K];
int dice[7] = { 0, 1,2,3,4,5,6 };
// 이동에 따른 주사위의 면 변화
int roll[5][7] = {
   {0, 0, 0, 0, 0, 0, 0},  // Dummy (0번 이동은 없음)
   {0, 5,2,1,4,6,3},  // 동쪽 (1번 이동)
   {0, 3,2,6,4,1,5},  // 서쪽 (2번 이동)
	// 북쪽 (3번 이동)
   {0, 2,6,3,1,5,4},   // 남쪽 (4번 이동)
   {0, 4,1,3,6,5,2}
};
int value[7];

// 격자 범위 확인
bool is_in_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < m;
}

void roll_dice(int direction) {
	int new_dice[7];
	for (int i = 1; i <= 6; ++i) {
		new_dice[i] = dice[roll[direction][i]];
	}
	for (int i = 1; i <= 6; ++i) {
		dice[i] = new_dice[i];
	}
}

int main() {
	// 입력 받기
	cin >> n >> m >> x >> y >> k;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < k; i++) {
		cin >> dir[i];
	}
	for (int i = 0; i < k; i++) {
		int direction = dir[i];

		int nx = x + dx[direction];
		int ny = y + dy[direction];

		if (!is_in_range(nx, ny)) continue;

		// 주사위 이동
		roll_dice(direction);

		// 바닥면(6번 면)과 격자 값 동기화
		if (map[nx][ny] == 0) { //
			map[nx][ny] = value[dice[6]];
		}
		else {
			
				value[dice[6]] = map[nx][ny];
				map[nx][ny] = 0;
		}


		// 위치 갱신
		x = nx;
		y = ny;

		// 윗면 출력
		cout << value[dice[1]] << endl;
	}

	return 0;
}
