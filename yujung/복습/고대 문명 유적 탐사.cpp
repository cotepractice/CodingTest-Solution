#include<iostream>
#include<queue>
#include<cstring>
#include<vector>
using  namespace std;
int k, m;
int map[5][5];
int tmp[5][5];
int tmp2[5][5];
bool visited[5][5];
queue<int> you;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int answer = 0;


bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < 5 && y < 5;
}


int bfs(int x, int y){
	queue<pair<int, int>> q;
	visited[x][y] = true;
	int first_num = tmp[x][y];
	int cnt = 1;
	q.push({ x,y });
	while (!q.empty()) {
		int a=q.front().first;
		int b = q.front().second;
		q.pop();
		for (int i = 0; i < 4;i++) {
			int nx = a + dx[i];
			int ny = b + dy[i];
			if (!is_range(nx, ny) ||visited[nx][ny]==true|| first_num != tmp[nx][ny]) { continue; }
			q.push({ nx,ny });
			visited[nx][ny] = true;
			cnt++;
		}
	}
	return cnt;
}

int check_num() {
	memset(visited, false, sizeof(visited));
	int sum = 0;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			if (visited[i][j] == false) {
				int n = bfs(i, j);
				if (n >= 3) {
					sum += n;
				}
			}
		}

	}
	return sum;
}
int bfs2(int x, int y) {
	queue<pair<int, int>> q;
	vector<pair<int, int>> v;
	visited[x][y] = true;
	int first_num = map[x][y];
	int cnt = 1;
	q.push({ x, y });
	v.push_back({ x, y });
	while (!q.empty()) {
		int a = q.front().first;
		int b = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = a + dx[i];
			int ny = b + dy[i];
			if (!is_range(nx, ny) || visited[nx][ny] == true || first_num != map[nx][ny]) {
				continue;
			}
			q.push({ nx, ny });
			v.push_back({ nx, ny });
			visited[nx][ny] = true;
			cnt++;
		}
	}
	if (cnt >= 3) {
		for (int l = 0; l < v.size(); l++) {
			int vx = v[l].first;
			int vy = v[l].second;
			map[vx][vy] = 0;
		}
	}
	return cnt;
}


void rotate(int x, int y, int num) {
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			tmp[i][j] = map[i][j];
		}
	}
	if (num == 1) {
		for (int i = x; i < x + 3; i++) {
			for (int j = y; j < y + 3; j++) {
				int ox = i - x;
				int oy = j - y;
				int cx = oy;;
				int cy = 2 - ox;
				tmp[x + cx][y + cy] = map[i][j];
			}
		}
	}
	if (num == 2) {
		for (int k = 0; k < 2; k++) {
			for (int i = x; i < x + 3; i++) {
				for (int j = y; j < y + 3; j++) {
					int ox = i - x;
					int oy = j - y;
					int cx = oy;;
					int cy = 2 - ox;
					tmp2[x + cx][y + cy] = tmp[i][j];
				}
			}

			for (int i = x; i < x + 3; i++) {
				for (int j = y; j < y + 3; j++) {
					tmp[i][j] = tmp2[i][j];
				}
			}
		}
	}


	if (num == 3) {
		for (int k = 0; k < 3; k++) {
			for (int i = x; i < x + 3; i++) {
				for (int j = y; j < y + 3; j++) {
					int ox = i - x;
					int oy = j - y;
					int cx = oy;;
					int cy = 2 - ox;
					tmp2[x + cx][y + cy] = tmp[i][j];
				}
			}

			for (int i = x; i < x + 3; i++) {
				for (int j = y; j < y + 3; j++) {
					tmp[i][j] = tmp2[i][j];
				}
			}
		}
	}

}


bool find_rect() {
	int max_v = 0;
	int max_x = -1;
	int max_y = -1;
	int max_num = 0;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			rotate(j, i, 1);
			int cur_v = check_num();
			if (max_v <cur_v ){
				max_v = cur_v;
				max_x = j;
				max_y = i;
				max_num = 1;
			}
		}
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			rotate(j, i, 2);
			int cur_v = check_num();
			if (max_v < cur_v) {
				max_v = cur_v;
				max_x = j;
				max_y = i;
				max_num = 2;
			}
		}
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			rotate(j, i, 3);
			int cur_v = check_num();
			if (max_v < cur_v) {
				max_v = cur_v;
				max_x = j;
				max_y = i;
				max_num = 3;
			}
		}
	}

	if (max_v == 0) {
		return false;
	}
	rotate(max_x, max_y, max_num);


	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			map[i][j] = tmp[i][j];
		}
	}
	bool f = true;
	answer = 0;
	while (f) {
		f = false;
		memset(visited, false, sizeof(visited));
	
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (visited[i][j] == false) {
					int cnt=bfs2(i, j);
					if (cnt >= 3) {
						f = true;
						answer += cnt;
					}
				}
			}
		}
		if (f == false) {
			break;
		}

		for (int i = 0; i < 5; i++) {
			for (int j = 4; j >= 0; j--) {
				if (map[j][i] == 0) {
					map[j][i] = you.front();
					you.pop();
				}
			}
		}
	}
	return true;
}


int main() {
	cin >> k >> m;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < m; i++) {
		int a;
		cin >> a;
		you.push( a );
	}

	while (k--) {
		int f = find_rect();
		if ( f== false) {
			break;
		}
		else {
			cout << answer<<" ";
		}
	}

}