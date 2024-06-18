#include<iostream>
#include<vector>
using namespace std;

int n, m;
bool visited[8];
vector<int> v;
int arr[8];

void dfs(int cnt) {
	if (cnt == m) {
		for (int i = 0; i < v.size(); i++) {
			cout << v[i]<<" ";
		}
		cout << "\n";
		return;
	}
	for (int i = 0; i < n; i++) {
		if (visited[i] == true)continue;
		visited[i] = true;
		v.push_back(arr[i]);
		dfs(cnt + 1);
		v.pop_back();
		visited[i] = false;
	}
}

int main() {

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		arr[i] = i + 1;
		visited[i] = false;
	}
	dfs(0);
}