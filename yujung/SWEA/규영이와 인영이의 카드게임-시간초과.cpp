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
int gyu_score = 0;
int in_score = 0;

void dfs(int cnt) {
	if (cnt == 9) {
		gyu_score = 0;
		in_score = 0;
		for (int i = 0; i < 9; i++) {
			if (gyu[i] > ans[i]) {
				gyu_score += gyu[i] + ans[i];
			}
			else {
				in_score += gyu[i] + ans[i];
			}
		}
		if (gyu_score > in_score) {
			win++;
		}
		else if (gyu_score < in_score) {
			lose++;
		}
		return;
	}
	for (int i = 0; i < 9; i++) {
		if (!visited[i]) {
			visited[i] = true;
			ans.push_back(v[i]); // 숫자는 1부터 9까지
			dfs(cnt + 1);
			ans.pop_back();
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
		dfs(0);
		cout << "#" << t << " "<<win << " " << lose<<"\n";
		v.clear();
		win = 0;
		lose = 0;
	}
	
}