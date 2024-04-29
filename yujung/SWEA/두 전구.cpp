#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

int map[101];
vector<int> v;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int a, b, c, d;
		int cnt = 0;
		memset(map, 0, sizeof(map));
		cin >> a >> b >> c >> d;
		for (int i = a; i <= b; i++) {
			map[i]++;
		}
		for (int i = c; i <= d; i++) {
			map[i]++;
			if (map[i] == 2) {
				cnt++;
			}
		}
		if (cnt != 0) {
			cnt--;
		}
		v.push_back(cnt);
	}
	for (int t = 1; t <= T; t++) {
		cout << "#" << t << " " << v[t-1] << "\n";
	}

}