#include<iostream>
#include<vector>
#define MAX_N 51
using namespace std;
int map[MAX_N][MAX_N]; //개수 관리
int n, m, k;
struct s {
	int r, c, m, s, d;
};
vector<s> v; //위치 관리

int dx[8] = {-1,-1,0,1,1,1,0,-1};
int dy[8] = {0,1,1,1,0,-1,-1,-1};

int r[4] = { 0,2,4,6 };
int c[4] = { 1,3,5,7 };
void move() {
	for (int i = 0; i < v.size(); i++) {
		s a=v[i];
		int s = a.s%n;
		int nx = (a.r + s*dx[a.d]);
		int ny = (a.c + s*dy[a.d]);
		if (nx >= n)nx -= n;
		if (ny >= n)ny -= n;
		if(nx< 0)nx+= n;
		if(ny< 0)ny+= n;
		map[a.r][a.c]--;//이동
		map[nx][ny]++;
		v[i].r = nx;
		v[i].c = ny;
	}
}

void happen() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] >= 2) {//2개 이상이라면
				int sum_j = 0; //질량합
				int sum_s = 0;//속력합
		
				bool f = false; //짝수인지 홀 수 인지
				bool f1 = false;
				int cnt = 0;
				for (int k = 0; k < v.size(); k++) {
					s a = v[k];
					if (i == a.r&&j == a.c) {
						sum_j += a.m;
						sum_s += a.s;

						if (a.d % 2 == 0) {//하나라도 짝수 이면
							f = true;
						}
						else {
							f1 = true;
						}
				
						v.erase(v.begin() + k,v.begin()+k+1);
						k--;
						cnt++;
					}
				}

				int mean_j = sum_j / 5;
				int mean_s= sum_s / cnt;
				for (int k = 0; k < 4; k++) {
					if (mean_j <= 0)break;
				
					else if ((f&&!f1)||(!f && f1)) {
						v.push_back({ i,j,mean_j,mean_s,r[k] });
					}
					else {
						v.push_back({ i,j,mean_j,mean_s,c[k] });
					}
						
					
				}
				if (mean_j > 0) {
					map[i][j] = 4;
				}
				else {
					map[i][j] = 0;
				}
				

			}
		}
	}
}
int main() {
	
	cin >> n >> m >> k;
	for (int i = 0; i < m; i++) {
		int r, c, m, s, d;
		cin >> r >> c>>m>>s>>d;
		v.push_back({ r - 1,c - 1, m,s,d });
		map[r-1][c-1]++;
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