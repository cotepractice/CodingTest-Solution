//열마다 res에 석유양을 저장하여 효율성 높임, 그러나 전보다 효율성이 증가하였으나 아직도 시간초과남

#include <string>
#include <vector>
#include<queue>
#include<set>
using namespace std;

bool visited[500][500];
int res[500];
queue<pair<int, int>> q;
vector<pair<int, int>> v;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
set<int> s;
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
				s.insert(ny);
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
				s.insert(j);
				int c = bfs(land);

				for (auto a:s) {
					res[a] += c;
				}
				s.clear();
			}
		}
	}


	int tmp = 0;
	for (int j = 0; j < m; j++) {
		answer = max(answer, res[j]);
	}

	return answer;
}
