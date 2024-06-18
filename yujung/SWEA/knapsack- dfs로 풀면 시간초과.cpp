#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<pair<int,int>> v;
int n, k;
int res = 0;
void dfs(int cnt, int cur_value,int price) {
	if (cur_value < 0)return;
	if (cnt == n)return;
	res = max(res, price);
	dfs(cnt + 1, cur_value - v[cnt].first, price + v[cnt].second);
	dfs(cnt + 1, cur_value , price );
}


int main() {

	
	int T;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			int a, b;
			cin >> a >> b;
			v.push_back({ a,b });
		}

		dfs(0, k, 0);
		cout <<"#"<<t<<" "<< res<<"\n";
	}
}

