#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

vector<pair<int,int>> v;
int n, k;
int res = 0;


int main() {

	
	int T;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> n >> k;
		int dp[101][1001];
		memset(dp, 0, sizeof(dp));
		for (int i = 0; i < n; i++) {
			int a, b;
			cin >> a >> b;
			v.push_back({ a,b });
		}
		//v[0]값이 있고 c[0]--> 무게 값

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= k; j++) {
				if (j >= v[i - 1].first) {
					dp[i][j] = max(dp[i-1][j - v[i - 1].first] + v[i - 1].second, dp[i-1][j]);
				}
				else {
					dp[i][j] = dp[i - 1][j];
				}
			}
		}
		cout <<"#"<<t<<" "<< dp[n][k]<<"\n";
        v.clear();	}
}

