
#include<iostream>
#include<vector>
#include<cstring>
#define MAX_N 50
using namespace std;


int map[MAX_N][MAX_N];
int dx[4] = { 0,1,0,-1 }; // 왼,아래, 오른쪽, 위,
int dy[4] = { -1,0, 1, 0 };
//↑, ↓, ←, →
int rx[5] = { 0, -1,1,0,0 };
int ry[5] = { 0,0,0,-1,1 };
int cnt[4];
vector<int> v;
int n, m;
int sx;
int sy;
int f = true;
//이상함 수정 필요
int score = 0;



void find_same() {

	bool ff = true; 

	while (ff) {
		ff = false; 
		vector<int> tmp2; 

		for (int i = 0; i < v.size(); i++) {
			int next = i; 

			if (v[i] != v[next]) {
				tmp2.push_back(v[i]);
			}
			else {
		
				while ( next < v.size()&& v[i] == v[next]) {
					next++;
				}

			
				if (next - i < 4) {
					for (int j = i; j < next; j++) {
						tmp2.push_back(v[j]);
					}
				}
				else {
					score += v[i] * (next - i);
					ff = true; 
				}
			}
			i = --next; 
		}
		v = tmp2; 
	}
}



void make_v2() {
	vector<int> tmp;

	for (int i = 0; i < v.size(); i++) {
		int next = i; 

		while ( next < v.size()&& v[i] == v[next] ) {
			next++;
		}

		tmp.push_back(next - i);
		tmp.push_back(v[i]);

	
		i = --next;
	}

	/*if (tmp.size() >= n * n) { 이거 해도 되고 안해도 되고 , 최적화를 위해 하는게 좋음
		while (tmp.size() >= n * n) {
			tmp.pop_back();
		}
	}*/
	v = tmp;
}

void init() {
	v.clear();
	int nx = n / 2 + 1;
	int ny = n / 2 + 1;
	int dir = 0;
	int length = 1;
	int num = 0;
	bool flag = false;

	while (1) {

		for (int i = 0; i < length; i++) {
			nx = nx + dx[dir];
			ny = ny + dy[dir]; //이동
			if (nx<1 || ny<1 || nx > n || ny > n) { flag = true; break; }
			if (map[nx][ny] > 0) {
				v.push_back(map[nx][ny]);
			}
		}

		if (flag)break;

		num++;
		dir++;
		if (dir == 4) {
			dir = 0;
		}
		if (num == 2) {
			num = 0;
			length++;
		}

	}
}

void copy() {
	memset(map, 0, sizeof(map));
	int nx = n / 2 + 1;
	int ny = n / 2 + 1;
	int dir = 0;
	int length = 1;
	int num = 0;
	bool f = false;

	while (v.size() > 0) {

		for (int i = 0; i < length; i++) {
			nx = nx + dx[dir];
			ny = ny + dy[dir]; //이동
			if (nx<1 || ny<1 || nx > n || ny > n) { f = true; break; }
			if (nx == n / 2 + 1 && ny == n / 2 + 1)continue;
			if (map[nx][ny] > 0) {
				v.push_back(map[nx][ny]);
			}
			if (v.empty())break;
			map[nx][ny] = v.front();
			v.erase(v.begin(), v.begin() + 1);
		}

		if (f)break;

		num++;
		dir++;
		if (dir == 4) {
			dir = 0;
		}
		if (num == 2) {
			num = 0;
			length++;
		}

	}

}
int main() {

	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> map[i][j];
		}
	}
	sx = n / 2 + 1;



	while (m--) {
		int ax = sx;
		int ay = sx;
		int a, b;
		cin >> a >> b; //거리 방향
		for (int i = 0; i < b; i++) {
			ax = ax + rx[a];
			ay = ay + ry[a];
			//		cnt[map[ax][ay]]++;
			map[ax][ay] = 0;//폭파
		}

		init();

		find_same();

		make_v2();

		copy();
	}

	int sum = 0;
	for (int i = 1; i <= 3; i++) {
		sum += i * cnt[i];
	}
	cout << score;
}