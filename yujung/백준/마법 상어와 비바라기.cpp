#include<iostream>
#include<cstring>
#define MAX_N 100
using namespace std;
//모든 구름이 di 방향으로 si칸 이동한다.
//각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
//구름이 모두 사라진다.
//2에서 물이 증가한 칸(r, c)에 물복사버그 마법을 시전한다.물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼(r, c)에 있는 바구니의 물이 양이 증가한다.
//이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
//예를 들어, (N, 2)에서 인접한 대각선 칸은(N - 1, 1), (N - 1, 3)이고, (N, N)에서 인접한 대각선 칸은(N - 1, N - 1)뿐이다.
//바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
//M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.

int n, m;
int A[MAX_N][MAX_N];
int cloud[MAX_N][MAX_N];
int tmp[MAX_N][MAX_N];
//←, ↖, ↑, ↗, →, ↘, ↓, ↙
int dx[9] = {0, 0,-1,-1,-1,0,1,1,1 };
int dy[9] = { 0,-1,-1,0,1,1,1,0,-1 };

int rx[4] = { -1,-1,1,1 };
int ry[4] = { -1,1,1,-1 };

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < n;
}
int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> A[i][j];
		}
	}

	cloud[n - 1][0] = 1;
	cloud[n - 1][1] = 1;
	cloud[n - 2][0] = 1;
	cloud[n - 2][1] = 1;

	while (m--) {
		int d, s; //방향 s칸
		cin >> d >> s;
		memset(tmp, 0, sizeof(tmp)); // tmp 배열 초기화
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (cloud[i][j] == 1) {
					int nx = (i + s * dx[d] + n*s) % n;
					int ny = (j + s * dy[d] + n*s) % n;
					tmp[nx][ny] = 1; // 구름 이동
					A[nx][ny]++; // 물 양 증가
				}
			}
		}

		//물복사 마법
	for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (tmp[i][j] == 1) {
					int cnt = 0;
					for (int k = 0; k < 4; k++) {
						int nx = i + rx[k];
						int ny = j + ry[k];

						if (!is_range(nx, ny)) continue;
						if (A[nx][ny] > 0) cnt++;
					}
					A[i][j] += cnt;
				}
			}
		}
		memset(cloud, 0, sizeof(cloud));
		
		//구름 생기기 
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (tmp[i][j] == 1 || A[i][j] < 2)continue;
				cloud[i][j] = 1;
				A[i][j] -= 2;
			}
		}
		memset(tmp, 0, sizeof(tmp));
	

	}

	
	int sum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (A[i][j] > 0) {
				sum += A[i][j];
			}
		
		}
	}
	cout << sum;
}


