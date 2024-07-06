#include<iostream>
#include<vector>
#include<cstring>
#define MAX_N 55
using namespace std;
int n, m, k;
struct s {
	int r, c, m, s, d;
};
vector<s> v; //위치 관리
vector<s> map[MAX_N][MAX_N];
int dx[8] = { -1,-1,0,1,1,1,0,-1 };
int dy[8] = { 0,1,1,1,0,-1,-1,-1 };

int r[4] = { 0,2,4,6 };
int c[4] = { 1,3,5,7 };

void move() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			map[i][j].clear();
		}
	}
	for (int i = 0; i < v.size(); i++) {
		s a = v[i];
		int s = a.s%n;
		int nx = (a.r + s * dx[a.d]+n) % n;
		int ny = (a.c + s * dy[a.d]+n) % n;
	

		map[nx][ny].push_back({ nx,ny,a.m,a.s,a.d });

		v[i].r = nx;
		v[i].c = ny;
	}
}

void happen() {
	vector<s> tmp;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j].size() == 0)continue;
			if (map[i][j].size() == 1) {
				tmp.push_back(map[i][j][0]);
				continue;
			}
		
				int sum_j = 0; //질량합
				int sum_s = 0;//속력합

				bool f = false; //짝수인지 홀 수 인지
				bool f1 = false;
				for (int k = 0; k < map[i][j].size(); k++) {
					s a = map[i][j][k];
					sum_j += a.m;
					sum_s += a.s;

					if (a.d % 2 == 0) {//하나라도 짝수 이면
						f = true;
					}
					else {
						f1 = true;
					}
				}
				int mean_j = sum_j / 5;
				int mean_s = sum_s / map[i][j].size();

				if (mean_j == 0)continue;
				if (f1 == false || f == false) {
					for (int k = 0; k < 4; k++) {
						tmp.push_back({ i,j,mean_j,mean_s,r[k] });
					}
				}
				else {
					for (int k = 0; k < 4; k++) {
						tmp.push_back({ i,j,mean_j,mean_s,c[k] });
					}
				}
			
		}
	}

	v = tmp;
}
int main() {

	cin >> n >> m >> k;
	for (int i = 0; i < m; i++) {
		int r, c, m, s, d;
		cin >> r >> c >> m >> s >> d;
		v.push_back({ r - 1,c - 1, m,s,d });
		map[r - 1][c - 1].push_back({ r - 1,c - 1, m,s,d });
	}
	while (k--) {
		move();
		happen();
	}
	int answer = 0;
	for (int i = 0; i < v.size(); i++) {
		answer += v[i].m;
	}
	cout << answer;
}