#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#define MAX_N 10
#define MAX_M 100 //바이러스의 개수
using namespace std;

int n, m, k;

int map[MAX_N][MAX_N];
int tmp[MAX_N][MAX_N];
vector<int> v[MAX_N][MAX_N];


int die[MAX_M];

int dx[8] = { 0,0,1,1,1,-1,-1,-1 };
int dy[8] = { 1,-1, 0,1,-1,0,1,-1 };
int d[MAX_N][MAX_N];
int visited[MAX_N][MAX_N];
bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < n&&y < n;
}
//만약 양분이 부족하여 본인의 나이만큼 양분을 섭취할 수 ㄷ없다면 즉시 죽
void play() {
	memset(d, 0, sizeof(d));
	memset(visited, 0, sizeof(visited));
	//1.  각각의 바이러스는 본인이 속한 1*1 크기의 칸에 있는 양분을 섭취한다. 
	//본인의 나이만큼 양분 섭취하며, 같은 칸에 
	int th; //몇번째인지
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++) {

			int die_idx = -1;
	
			sort(v[i][j].begin(), v[i][j].end());
			for (int k = 0; k < v[i][j].size(); k++) {
				int a = map[i][j] - v[i][j][k];
				if (a>=0) //0보다 크면
				{
					map[i][j] = a;
					v[i][j][k]++; //바이러스 1만큼 커짐
				}
				else {
					die_idx = k;
					d[i][j] = die_idx;
					visited[i][j] = 1;
					break;
				}
			}

			

		}
	}

	//2. 모든 바이러스가 섭취를 끝낸 후 죽은 바이러스가 양분으로 변함

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (d[i][j] == -1||visited[i][j]==0)continue;
			for (int k = d[i][j]; k < v[i][j].size(); k++) {
				map[i][j] += v[i][j][k] / 2;
			}
			v[i][j].erase(v[i][j].begin() + d[i][j], v[i][j].end());
			
				
		}
	}
	//3. 이후 바이러스가 번식을 진행. 번식은 5의 배수의 나이를 
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < v[i][j].size(); k++) {
				if (v[i][j][k] % 5 == 0) //5의 배수인 경우
				{

					for (int g = 0; g < 8; g++) {
						int nx = i + dx[g];
						int ny = j + dy[g];
						if (!is_range(nx, ny))continue; //범위를 벗어나면
						v[nx][ny].push_back(1);
					}
				}
			}
		}
	}

	//4. 주어진 양분에 따라 주어짐
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			map[i][j]+=tmp[i][j]; //1이 주어짐
		}
	}
}

int main() {
	cin >> n >> m >> k;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> tmp[i][j];
			map[i][j] = 5;
		}
	}
	for (int i = 0; i < m; i++) {
		int x, y, age;
		cin >> x >> y >> age;
		v[x-1][y-1].push_back(age);
	}
	while (k--) {
		play();
	}

	int ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			ans += v[i][j].size();
		}
	}
	cout << ans;
}