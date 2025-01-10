#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
int map[1025][1025];

int recur(int n , int x, int y) {
	if (n == 2) {
		vector<int> v;
		for (int i = x; i < x + 2; i++) {
			for (int j = y; j < y + 2; j++) {
				v.push_back(map[i][j]);
			}
		}
		sort(v.begin(), v.end());
		return v[1];
	}
	vector<int> v;

	v.push_back(recur(n / 2, x, y));
	v.push_back(recur(n / 2, x, y + n / 2));
	v.push_back(recur(n / 2, x + n / 2, y));
	v.push_back(recur(n / 2, x + n / 2, y + n / 2));
	sort(v.begin(), v.end());
	return v[1];
}
int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> map[i][j];
		}
	}
	cout<<recur(n, 1, 1);
}