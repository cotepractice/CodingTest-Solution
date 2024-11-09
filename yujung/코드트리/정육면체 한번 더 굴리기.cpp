#include <iostream>
#include <queue>
using namespace std;

#define MAX_N 20
int n, m;
int map[MAX_N][MAX_N];
int cur_dice[7] = { 0, 1, 2, 3, 4, 5, 6 };
int tmp[7];
bool visited[MAX_N][MAX_N];

// 동, 남, 서, 북 방향 주사위 회전 정의
int dir[4][7] = {
	{0, 4, 2, 1, 6, 5, 3}, // 동
	{0, 5, 1, 3, 4, 6, 2}, // 남
	{0, 3, 2, 6, 1, 5, 4}, // 서
	{0, 2, 6, 3, 4, 1, 5}  // 북
};

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int rr = 0, rc = 0;  // 주사위의 현재 위치
int rd = 0;  // 초기 방향 (0: 동쪽)
int ans = 0;

// 격자 범위 확인
bool is_in_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < n;
}

// BFS로 같은 숫자의 연결된 칸을 탐색하여 점수를 계산
int bfs(int x, int y) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visited[i][j] = false;
		}
	}

	int cnt = 1;
	queue<pair<int, int>> q;
	visited[x][y] = true;
	int cmp = map[x][y];
	q.push({ x, y });
	int score = 0;

	while (!q.empty()) {
		int cx = q.front().first;
		int cy = q.front().second;
		q.pop();
		score += cmp;

		for (int i = 0; i < 4; i++) {
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			if (!is_in_range(nx, ny) || visited[nx][ny]) continue;
			if (cmp == map[nx][ny]) {
				cnt++;
				q.push({ nx, ny });
				visited[nx][ny] = true;
			}
		}
	}
	return score;
}

// 주사위의 현재 상태를 이동 방향에 따라 변경
void move_dice() {
	for (int i = 1; i <= 6; i++) {
		tmp[i] = cur_dice[dir[rd][i]];
	}
	for (int i = 1; i <= 6; i++) {
		cur_dice[i] = tmp[i];
	}
}

// 게임 한 턴을 실행
void play() {
	int nx = rr + dx[rd];
	int ny = rc + dy[rd];

	// 격자 밖으로 나가면 방향을 반대로 변경
	if (!is_in_range(nx, ny)) {
		rd = (rd + 2) % 4;
		nx = rr + dx[rd];
		ny = rc + dy[rd];
	}

	// 위치 및 주사위 이동
	rr = nx;
	rc = ny;
	move_dice();

	// 바닥면 주사위 숫자와 격자 숫자 비교하여 방향 결정
	int bottom_num = cur_dice[6];
	if (bottom_num > map[rr][rc]) { // 시계방향 회전
		rd = (rd + 1) % 4;
	}
	else if (bottom_num < map[rr][rc]) { // 반시계 방향 회전
		rd = (rd + 3) % 4;
	}

	// 점수 합산
	ans += bfs(rr, rc);
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}

	while (m--) {
		play();
	}

	cout << ans;
	return 0;
}
