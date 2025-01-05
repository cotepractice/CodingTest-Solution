#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int n;

int board[1025][1025];
int recur(int n, int x, int y) {
	if (n == 2)
	{
		vector<int> v;
		for (int i = x; i < x + 2; i++) {
			for (int j = y; j < y + 2; j++) {
				v.push_back(board[i][j]);
			}
		}
		sort(v.begin(), v.end());
		return v[2];
	}
	vector<int> v;
	v.push_back(recur(n / 2, x, y));
	v.push_back(recur(n / 2, x, y + n / 2));
	v.push_back(recur(n / 2, x + n / 2, y));
	v.push_back(recur(n / 2, x + n / 2, y + n / 2));
	sort(v.begin(), v.end());
	return v[2];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> board[i][j];
		}
	}
	cout << recur(n, 1, 1);

}