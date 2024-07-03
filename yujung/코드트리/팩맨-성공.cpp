#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
#define MAX_M 11
#define MAX_N 5
int m, t; //몬스터의 마리 수 m과 진행되는 턴의 수 t
int sx, sy; //팩맨
int r, c, d;
struct  s {
	int x;
	int y;
	int d;
	int islive; //죽었는지 확인
};

vector<s> tmp;
vector<s> v;

int map[MAX_N][MAX_N]; //몬스터 개수
int die[MAX_N][MAX_N]; //죽은 블록, 3으로 기록했다가 감소


int dx[9] = { 0,-1,-1,0,1,1,1,0,-1 }; //↑, ↖, ←, ↙, ↓, ↘, →, ↗
int dy[9] = { 0,0,-1,-1,-1,0,1,1,1 };

int rx[4] = { -1,0,1,0 };//상,좌,하,우
int ry[4] = { 0,-1,0,1 };
int mx = 0;
int my = 0;
int max_v = -1;
bool visited[MAX_N][MAX_N];
vector<int> q;
vector<int> route;




bool is_range(int x, int y) {
	return 0 < x && 0 < y && x < 5 && y < 5;
}


int monster_cnt() {
	memset(visited, false, sizeof(visited));
	int x = sx;
	int y = sy;
	int monster_num = 0;
	for (int i = 0; i < 3; i++) {
		int dir = q[i];
		int nx = x + rx[dir];
		int ny = y + ry[dir];

		if (!is_range(nx, ny))return -1;

		if (visited[nx][ny] == false) {
			monster_num += map[nx][ny];
			visited[nx][ny] = true;
		}
		x = nx;
		y = ny;
	}
	return monster_num;
}
void dfs(int cnt, int x, int y, int sum) {
	if (cnt == 3) {
		if (max_v < monster_cnt()) {
			max_v = monster_cnt();
			route = q;
		}
		return;
	}

	for (int i = 0; i < 4; i++) {
		int nx = x + rx[i];
		int ny = y + ry[i];

		if (!is_range(nx, ny)) continue;

		q.push_back(i); // i 대신 방향 인덱스 저장

		dfs(cnt + 1, nx, ny, sum + map[nx][ny]);


		q.pop_back();
	}
}

void sosil() {
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++) {
			if (die[i][j] > 0) {
				die[i][j]--;
			}
		}
	}
}

void copy_moster() {
	for (int i = 0; i < tmp.size(); i++) {
		v.push_back(tmp[i]);
		map[tmp[i].x][tmp[i].y]++;
	}

}
void ccopy() {
	tmp.clear();
	for (int i = 0; i < v.size(); i++) {
		if (v[i].islive == 1)continue;
		tmp.push_back(v[i]);
	}
}
void play() {
	ccopy(); //복제

	for (int i = 0; i < v.size(); i++) {
		if (v[i].islive == 1)continue; //죽은 경우임
		int x = v[i].x;
		int y = v[i].y;
		int d = v[i].d;
		d--;
		int num = 8;
		while (num--) {
			d++;

			if (d == 9) { d = 1; }

			int nx = (x + dx[d]);
			int ny = (y + dy[d]);

			//반시계 방향
			if (!is_range(nx, ny))continue;
			if (die[nx][ny])continue; //시체가 있거나
			if (sx == nx && sy == ny)continue; //팩맨이 잇거나

			v[i] = { nx,ny,d }; //이동
			map[x][y]--;
			map[nx][ny]++;

			break;

		}

	}
	max_v = -1;
	//q.clear();

	dfs(0, sx, sy, 0); //최대 몬스터 찾기
	//find_route(0);
	int nx = sx;
	int ny = sy;
	for (int i = 0; i < 3; i++) {
		nx = nx + rx[route[i]];
		ny = ny + ry[route[i]];
		if (map[nx][ny] > 0) {
			map[nx][ny] = 0;
			for (int j = 0; j < v.size(); j++) {
				if (nx == v[j].x&&ny == v[j].y) {
					v[j].islive = 1; //죽었음
				}
			}
			die[nx][ny] = 3; //사라지는 경우
		}

	}
	sx = nx;
	sy = ny;

	sosil(); //몬스터 시체 소멸

	copy_moster();



}
int main() {
	cin >> m >> t;
	cin >> sx >> sy;
	for (int i = 0; i < m; i++) {
		int r, c, d;
		cin >> r >> c >> d;
		v.push_back({ r,c,d });
		map[r][c]++;
	}
	while (t--) {
		play();
	}
	int sum = 0;
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++) {
			sum += map[i][j];
		}
	}

	cout << sum;
}