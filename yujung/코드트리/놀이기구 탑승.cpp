#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#define MAX_N 20
#define MAX_M 400
#define MAX_S 5
using namespace std;




int n;

map<int, vector<int>> arr;// ree->

struct s
{
	int x, y;
	int f = 0; //친구 수
	int  e = 0; //비어 있는 수
};
vector<s> v;
int f[MAX_N][MAX_N];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int m[MAX_N][MAX_N];
int cnt = 0;
int empty_[MAX_N][MAX_N];
int ans = 0;
int score[5] = { 0,1,10,100,1000 };
bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < n;
}
int sunseo[MAX_M];

bool cmp(s a, s b) {
	if (a.f != b.f)
	{
		return a.f > b.f;
	}
	else if (a.e != b.e) //만약 1번 조건을 만족하는 칸의 위치가 여러 곳이라면, 그 중 인접한 칸 중 
	{
		return a.e > b.e;
	}
	else if (a.x != b.x)
	{
		return a.x < b.x;
	}
	else {
		return a.y < b.y;
	}
}
void init() {

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++) {
			if (m[i][j] != 0) {
				f[i][j] = -1; //누가 있으면
			}
			else {
				int num = 0;
				for (int k = 0; k < 4; k++) {
					int hak = arr[sunseo[cnt]][k]; //학생
					for (int z = 0; z < 4; z++) {
						int nx = i + dx[z];
						int ny = j + dy[z];
						if (!is_range(nx, ny))continue;
						if (hak == m[nx][ny]) {
							num++;
							break;
						}

					}
				}
				f[i][j] = num;
			}
		}
	}
	
}

void init2() //empty 채우기
{
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (m[i][j] != 0) { //map이 0보다 크다면
				empty_[i][j] = -1; //이미 누가 있는 것임
			}
			else
			{
				int cnt = 0;
				for (int k = 0; k < 4; k++) {
					int nx = i + dx[k];
					int ny = j + dy[k];
					if (!is_range(nx, ny))continue;
					if (m[nx][ny] == 0) {
						cnt++;
					}
				}
				empty_[i][j] = cnt;
			}

		}
	}
}

void play() {
	init();
	init2();
	v.clear();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (m[i][j])continue; //이미 사람이 있으면 건너띔
			//사람이 없으면
			v.push_back({ i,j,f[i][j], empty_[i][j] });

		}
	}
	sort(v.begin(), v.end(), cmp);
	m[v[0].x][v[0].y] = sunseo[cnt];
	cnt++;
}
void result() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int p = m[i][j];
			int res = 0;
			for (int k = 0; k < 4; k++) {
				int com = arr[p][k];
				for (int z = 0; z < 4; z++) {
					int nx = i + dx[z];
					int ny = j + dy[z];
					if (!is_range(nx, ny))continue;
					if (com == m[nx][ny]) {
						res++;
						break;
					}
				}
			}
			ans += score[res];
		}
	}
}
int main() {
	cin >> n;

	for (int i = 0; i < n*n; i++)
	{
		for (int j = 0; j < 5; j++) {
			int a;
			if (j == 0) {
				cin >> a;
				sunseo[i] = a;
			}
			else {
				int b;
				cin >> b;
				arr[sunseo[i]].push_back(b);
			}
		}
	}

	for (int i = 0; i < n*n; i++)
	{
		play();
	}
	result();
	cout << ans;
}