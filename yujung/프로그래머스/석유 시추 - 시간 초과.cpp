#include <string>
#include <vector>
#include<queue>

using namespace std;

bool visited[500][500];
queue<pair<int, int>> q;
vector<pair<int, int>> v;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

bool is_ragne(int x, int y, int n, int m) {
	return x >= 0 && y >= 0 && x < n&& y < m;
}
int bfs(vector<vector<int>> land) {
	int n = land.size();
	int m = land[0].size();
	int cnt = 1;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (!is_ragne(nx, ny, n, m) || visited[nx][ny] == true)continue;
			visited[nx][ny] = true;
			if (land[nx][ny] == 1) {
				cnt++;
				v.push_back({ nx,ny });
				q.push({ nx,ny });
			}
		}
	}
	return cnt;
	

}
int solution(vector<vector<int>> land) {
	int answer = 0;
	int n = land.size();
	int m = land[0].size();

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (visited[i][j] == false && land[i][j] == 1) {
				visited[i][j] = true;
				q.push({ i,j });
				v.push_back({ i,j });
				int c=bfs(land);

				for (int i = 0; i < v.size(); i++) {
					int x = v[i].first;
					int y = v[i].second;
					land[x][y] = c;
				}
				v.clear();
			}
		}
	}

	
	int tmp = 0;
	for (int j = 0; j < m; j++) {
		bool f = false;
		tmp = 0;

		for (int i = 0; i < n; i++) {
			if (land[i][j] != 0 && f == false) {
				f = true;
				tmp += land[i][j];
			}
			else if (land[i][j] == 0) {
				f = false;
			}
		}
		
		answer = max(answer, tmp);
	}

	return answer;
}

