//반시계 방향으로 
#include<iostream>
#include<cstring>
using namespace std;
#define MAX_N 50


int map[MAX_N][MAX_N];
int tmp[MAX_N][MAX_N];
int tmp2[MAX_N][MAX_N];
int n, m, t;
int ex, ey;
int ex1, ey1;
int dx[4] = {0,-1,0,1}; //반시계 방향
int dy[4] = {1,0,-1,0};

int rx[4] = { 0,1,0,-1 }; //시계, 아래
int ry[4] = { 1,0,-1,0 };

void copy(int  arr[MAX_N][MAX_N], int  arr2[MAX_N][MAX_N]) { //복사
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			arr[i][j] = arr2[i][j];
		}
	}
}

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < m;
}

void spread() {
	memset(tmp2, 0, sizeof(tmp));
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++) {
			int a = map[i][j] / 5;
			int minus = 0;
			for (int k = 0; k < 4; k++) {
				int nx = i + dx[k];
				int ny = j + dy[k];
				if (!is_range(nx, ny) || map[nx][ny]==-1)continue;
				minus += a;
				tmp2[nx][ny] += a;
			}
			tmp2[i][j] -= minus;
		 }
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			map[i][j] += tmp2[i][j];
		}
	}
}
void second() { //회전
	//아래 행은 값은데 오른쪽으로 한칸씩 이동
	copy(tmp,map);
	for (int col = 0; col <m-1; col++) { //열
		if (col == 0) {
			map[ex][col+1] = 0;
			continue;
		}
		map[ex][col+1] = tmp[ex][col];
	}
	for (int row = ex; row > 0; row--) {  //행
		map[row - 1][m-1] = tmp[row][m-1];
	}
	for (int col = m-1; col > 0; col-- ) //co
	{
		map[0][col - 1] = tmp[0][col];
	}
	for (int row = 0; row < ex-1; row++)
	{
		map[row+1][0]=tmp[row][0];

	}

	//아래 반대
	for (int i = 0; i < m-1; i++) {
		if (i == 0) {
			map[ex1][i + 1] = 0;
			continue;
		}
		map[ex1][i + 1] = tmp[ex1][i];
	}
	for (int i = ex1; i < n-1; i++) {
		map[i + 1][m-1] = tmp[i][m-1];
	}

	for (int i = m-1; i > 0; i--) {
		map[n-1][i - 1] = tmp[n-1][i];
	}

	for (int i = n-1; i >ex1+1; i--) {
		map[i - 1][0] = tmp[i][0];
	}
}


int main() {
	cin >> n >> m >> t;
	int f = false;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
			if (map[i][j] == -1&&f==false) {
				ex = i;
				ey = j;
				f = true;
			}
			else if (map[i][j] == -1 && f == true) {
				ex1 = i;
				ey1 = j;
			}
		}
	}
	

	while (t--) {
		spread();
		second();
	}
	int ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == -1)continue;
			ans += map[i][j];
		}
	}
	cout << ans;
}