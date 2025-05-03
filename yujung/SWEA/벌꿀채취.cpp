#include<iostream>
#include<vector>
#define MAX_N 10
using namespace std;
int N,M,C;
bool visited[MAX_N];
int map[MAX_N][MAX_N];
vector<int> tmp;
vector<pair<int,pair<int,int>>> v;

int max_v = -1;
void dfs(int r, int c1, int c2) {
	for (int i = c1; i < c2 + M; i++)
	{
		if (visited[i] == true)continue;
		visited[i] = true;
		tmp.push_back({ map[r][i] });
		dfs(r, i+1, c2);
		visited[i] = false;
		tmp.pop_back();
	}
	int sum_v=0;
	for (int i = 0; i < tmp.size(); i++) {
		sum_v += tmp[i];
	}
	if (sum_v <= C)
	{
		int sum_v2 = 0;
		for (int i = 0; i < tmp.size(); i++) {
			sum_v2 += tmp[i]*tmp[i];
		}
		v.push_back({ sum_v2,{r,c2 } });
	}
}


void func() {
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N - M + 1; c++)
		{
			dfs(r, c, c); //첫번째 r은 변하도록
		}
	}

	for (int i = 0; i < v.size(); i++)
	{
		int first_v = v[i].first;
		int r1 = v[i].second.first;
		int c1 = v[i].second.second;
		for (int j = i+1; j < v.size(); j++) {
			int r2 = v[j].second.first;
			int c2 = v[j].second.second;
			int second_v = v[j].first;
			if (r1 == r2 && (r1+M  >= c2+1 ))
			{
				continue;
			}
			int res_v =first_v + second_v;
			if (max_v < res_v) {
				max_v = res_v;
			}

		}
	}
}


int main() {

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cin >> N >> M >> C;

		max_v = -1;
		v.clear();
		for (int i = 0; i < N; i++)
		{
			visited[i] = false;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++)
			{
				cin >> map[i][j];
			}
		}

		func();

		cout <<"#"<<t<<" "<< max_v<<endl;
	}
	



}