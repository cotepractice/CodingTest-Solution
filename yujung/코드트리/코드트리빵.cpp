#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;
# define MAX_N 15
# define MAX_M 30
# define INIT_M make_pair(-1,-1)
int board[MAX_N][MAX_N];
vector<pair<int,int>> c;//편의점 위치
vector<pair<int, int>> p; //사람의 위치

int n, m;
bool visited[MAX_N][MAX_N];
int step[MAX_N][MAX_N];
int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

bool is_range(int x, int y) {
	return(0 <= x && x < n&& 0 <= y && y < n);
}

void bfs(int x, int y) {
	
	memset(visited, false, sizeof(visited));
	queue<pair<int, int>>q;
	q.push({ x,y });
	visited[x][y] = true;
	step[x][y] = 0;
	while (!q.empty()) {
		pair<int, int> cur = q.front();
		q.pop();
		int px = cur.first;
		int py = cur.second;
		for (int i = 0; i < 4; i++) {
			int nx = px + dx[i];
			int ny = py + dy[i];
			//방문하지 않아야 하고
			//범위를 벗어나지 않아야 함
			//방문할 수 없는 경우가 있음
			if (visited[nx][ny] == true)continue;
			if (!is_range(nx, ny))continue;
			if (board[nx][ny] == 2)continue;
			step[nx][ny] = step[px][py]+1;
			visited[nx][ny] = true;
			q.push({ nx,ny });
		}
	}
}


void first(int current_t) {
	//편의점 방향을 향해 이동
	for (int i = 0; i < m; i++) {
		if (p[i] == INIT_M||p[i]==c[i])continue; //초기 위치에 있으면
		 
		bfs(c[i].first, c[i].second);
		int min = 10000;
		int min_x = -1;
		int min_y = -1;
		

		for (int j = 0; j < 4; j++) {
			int cx = p[i].first + dx[j];
			int cy = p[i].second + dy[j];
			if (board[cx][cy]!=2&&is_range(cx, cy) && min > step[cx][cy]) {
				
				min = step[cx][cy];
				min_x = cx;
				min_y = cy;
			}
		}

		p[i] = { min_x,min_y };
	}

	for (int i = 0; i < m; i++) {
		//if (p[i] == INIT_M && p[i] == c[i])continue; //초기 위치에 있으면
		if (p[i] == c[i])board[p[i].first][p[i].second] = 2;
	}

	if (current_t > m)return;


	bfs(c[current_t-1].first, c[current_t-1].second);
	int min = 10000;
	int min_x = -1;
	int min_y = -1;
	for (int j = 0; j < n; j++) {
		for (int k = 0; k < n; k++) {
			if (visited[j][k]&&board[j][k] == 1 && min > step[j][k]) {//2인 경우는 안돼
				min = step[j][k];
				min_x = j;
				min_y = k;
			}
		}
	}
	p[current_t - 1] = { min_x,min_y };
	board[min_x][min_y] = 2;
	
}

bool arrive_check() {
	for (int i = 0; i < m; i++) {
		if (c[i] != p[i]) return false;
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
		}
	}
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		c.push_back({ a-1,b-1 });
		p.push_back(INIT_M); //초기화
	}
	int t = 0;


	while (true)
	{
		t++;
		first(t);
		if (arrive_check())break;
	}
	cout << t;
}