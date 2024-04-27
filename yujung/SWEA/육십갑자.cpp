#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<string> v1;
vector<string> v2;
vector<string> ans;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			string a;
			cin >> a;
			v1.push_back(a);
		}
		for (int i = 0; i < m; i++) {
			string b;
			cin >> b;
			v2.push_back(b);
		}

		int q;
		string answer;
		cin >> q;
		for (int i = 0; i < q; i++) {
			int next;
			cin >> next;
			int tmp = 0;
			int tmp2 = 0;
			if ((next % n) == 0) {
				tmp = n - 1;
			}
			else {
				tmp = next % n - 1;
			}

			if ((next % m) == 0) {
				tmp2 = m - 1;
			}
			else {
				tmp2 = next % m - 1;
			}
			ans.push_back(v1[tmp] + v2[tmp2]);
		}
		
		cout << "#" << t << " ";
		for (auto a : ans) {
			cout << a<<" ";
		}
		cout << "\n";
		ans.clear();
		v1.clear();
		v2.clear();
	}
	
}