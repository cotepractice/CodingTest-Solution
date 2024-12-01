#include<iostream>
#define MAX_N 51
#define MAX_M 51
using namespace std;

int n, m;
int map[MAX_N][MAX_M];
bool visited[MAX_N][MAX_M];

int dx[4] = { -1, 0, 1, 0 }; //북, 동, 남, 서
int dy[4] = { 0, 1, 0, -1 };

int sx, sy, sd; // 시작 좌표 및 방향 (sx, sy: x, y 좌표, sd: 방향)
bool flag = false;
int cnt = 0;

// 함수: 이동 시도
void go() {
	// 현재 위치가 방문 처리된 상태로 시작
	visited[sx][sy] = true;
  // 처음 시작 위치 방문

	// 이동을 계속 시도
	while (!flag) {
		bool moved = false;
		for (int i = 0; i < 4; i++) {
			// 좌회전(현재 방향에서 1회전) 후 1칸 전진 시도
			sd = (sd + 3) % 4;  // 3을 더하는 방식으로 좌회전 (0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2)
			int nx = sx + dx[sd];
			int ny = sy + dy[sd];

			// 이동할 좌표가 유효하고, 해당 좌표가 벽이 아니며, 방문한 적이 없다면
			if ( !visited[nx][ny] && map[nx][ny] != 1) {
				// 해당 좌표로 이동
				sx = nx;
				sy = ny;
				visited[sx][sy] = true;  // 방문 처리
				cnt++;  // 방문 횟수 증가
				moved = true;
				break;  // 한 번 이동했으면 반복문 종료
			}
		}

		// 만약 4방향 모두 갈 수 없다면 후진 시도
		if (!moved) {
			  // 후진 방향
			int nx = sx - dx[sd];
			int ny = sy - dy[sd];

			// 후진이 가능하면 후진
			if ( map[nx][ny] != 1) {
				sx = nx;
				sy = ny;
				cnt++;  // 후진 후 방문 처리
			}
			else {
				// 후진도 불가능하면 종료
				flag = true;
			}
		}
	}
}

int main() {
	cin >> n >> m;
	cin >> sx >> sy >> sd;

	// 지도 입력 받기
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	// 자율 주행 함수 실행
	go();

	// 결과 출력: 방문한 칸의 수
	int ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (visited[i][j]) {
				ans++;
			}
		}
	}
	cout << ans;
	return 0;
}
