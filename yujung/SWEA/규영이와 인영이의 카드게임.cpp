#include <iostream>
#include<vector>
#include<cstring>
using namespace std;


int arr[19];
bool visited[9];
vector<int> ans;
vector<int> v;
int win = 0;
int lose = 0;
int gyu[9];//규영


void dfs(int cnt, int gyu_score,int iy_score) {
	if (cnt == 9) {
	
		
		if (gyu_score > iy_score) {
			win++;
		}
		
		return;
	}
	for (int i = 0; i < 9; i++) {
		if (!visited[i]) {
			visited[i] = true;
			if (gyu[cnt] > v[i]) { dfs(cnt + 1, gyu_score + gyu[cnt] + v[i], iy_score); }
			else { dfs(cnt + 1, gyu_score, iy_score + gyu[cnt] + v[i]); }
			visited[i] = false;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		
		memset(arr, 0, sizeof(arr));

		for (int i = 0; i < 9; i++) {
			int a;
			cin >> a;
			gyu[i] = a;
			arr[a]++;
		}
		

		for (int i = 1; i <= 18; i++) {

			if (arr[i] == 0) {
				v.push_back(i);
			}
		}
		
		memset(visited, false, sizeof(visited));
		dfs(0,0,0);
		cout << "#" << t << " "<<win << " " << 362880-win<<"\n";
		v.clear();
		win = 0;
		lose = 0;
	}
	
}