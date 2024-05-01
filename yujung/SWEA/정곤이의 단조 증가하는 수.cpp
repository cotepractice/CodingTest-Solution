#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

bool check(int n) {
	string s = to_string(n);
	for (int i = 0; i < s.size()-1; i++) {
		if (s[i] > s[i + 1]) {
			return false;
		}
	}
	return true;
}


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		vector<int> v;
		for (int i = 0; i < n; i++) {
			int a;
			cin >> a;
			v.push_back(a);
		}

		int ans = -1;
		for (int i = 0; i < v.size() - 1; i++) {
			for (int j = i + 1; j < v.size(); j++) {
				int res = v[i] * v[j];
				if (check(res) == true) {
					ans = max(ans, res);
				}
			}
		}
		cout <<"#"<<t<<" "<<ans<<"\n";
	}
	
}