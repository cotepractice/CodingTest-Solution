#include<iostream>
#include<vector>
#include<queue>
using namespace std;
#define MAX_N 6
int n;
int t;
char map[MAX_N][MAX_N];

vector<int> v;
vector<pair<int, int>> T;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
bool flag=false;
bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < n&&y < n;
}

bool bfs()
{
	bool f = true;
	for (int i = 0; i < T.size(); i++) {
		int cx = T[i].first;
		int cy = T[i].second;

		for (int j = 0; j < 4; j++) {
			int nx = cx;
			int ny = cy;
			while (1) {
				nx = nx + dx[j];
				ny = ny + dy[j];
				if (!is_range(nx, ny) || map[nx][ny] == 'O') { //범위를 벗어난다면, -> 
					break;
				}
				if (map[nx][ny] == 'S')
				{
					f = false;
					break;
				}
			}
			if (f == false) {
				return false;
			}
		}
	}
	return true;


}

void dfs(int cnt, int idx)
{ 
	if (flag == true) {
		return;
	}

	if (cnt == 3) { //cnt가 3이면
		bool f = true;
		for (int i = 0; i < v.size(); i++) {
			int row = v[i] / n;
			int col = v[i] % n;
			if (map[row][col] != 'X')
			{
				f = false; //벽이 들어갈 수 없음
			}
			
		}

		if(f==true)
		{
			for (int i = 0; i < v.size(); i++)
			{
				int row = v[i] / n;
				int col = v[i] % n;
				map[row][col] = 'O';
			}

			flag = bfs();

			if (flag == false) {
				for (int i = 0; i < v.size(); i++)
				{
					int row = v[i] / n;
					int col = v[i] % n;
					map[row][col] = 'X';
				}
			}
		 }

		
		
		return;
	}
	for (int i = idx; i < t; i++) {
		v.push_back(i);
		dfs(cnt + 1, idx + 1);
		v.pop_back();
	}
		
}


int main() {
	cin >> n;
	t = n * n ;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			if (map[i][j] == 'T')
			{
				T.push_back({ i,j });
			}
			
		}
	}

	dfs(0,0);

	if (flag == true) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}


}