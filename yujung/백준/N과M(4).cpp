#include<iostream>
#include<vector>
using namespace std;
#define MAX 8
int n, m;
int visited[MAX];
vector<int> v;
void dfs(int cnt,int idx) {
	
	if (cnt==m) { //visited[i]가 true이면, 
		for (int i = 0; i < m; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = 0; i < n; i++) {
		v.push_back(i+1);
		dfs(cnt + 1,i+1);
		v.pop_back();
		
	}
}

int main() {
	
	cin >> n >> m;
	dfs(0,0);
}
