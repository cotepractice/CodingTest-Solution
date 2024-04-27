#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int n, m;
int visited[100];
vector<string> v;
vector<string> arr;
int answer = 0;
bool flag = false;
int cnt = 0;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		answer = 0;
		cnt = 0;
		flag = false;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			string a;
			cin >> a;
			if (a != string(a.rbegin(), a.rend())) {
				v.push_back(a);
			}
			else {
				flag = true;
			}
		}
		while (!v.empty()) {
			string a = v.back();
			v.pop_back();
			string tmp = a;
			reverse(tmp.begin(), tmp.end());
			if (find(v.begin(), v.end(), tmp) != v.end()) {
				cnt += 2;
			}
		}
		answer = cnt * m;
		if (flag) {
			answer += m;
		}
		cout << "#" << t << " " << answer << "\n";
		
	}
	
}