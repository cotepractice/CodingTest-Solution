#include<iostream>
#include<vector>
#include<string>
#include<map>
#define MAX_N 4
using namespace std;

vector<int> v[MAX_N];
map<int, int> m;
bool is_range(int x) {
	return x >= 0 && x < 4;
}
void right(int n) {
	int b = v[n].back();
	v[n].pop_back();
	v[n].insert(v[n].begin(), b);
}
void left(int n) {
	int a = v[n].front();
	v[n].erase(v[n].begin(), v[n].begin() + 1);
	v[n].push_back(a);
}
void rotate(int n, int d) {
	if (d == 1) { //시계방향
		right(n);


	}
	else { //반시계 방향
		left(n);
	}
}

void dfs_left(int n, int d) {
	if (!is_range(n - 1))return;
	if (v[n - 1][2] != v[n][6])
	{
		if (d == 1) {
			d = -1;
		}
		else {
			d = 1;
		}
		m[n - 1] = d;
		//반대 방향으로 회전
		dfs_left(n - 1, d);
	}
}


void dfs_right(int n, int d)
{
	if (!is_range(n + 1))return;
	if (v[n][2] != v[n + 1][6]) {
		if (d == 1) {
			d = -1;
		}
		else {
			d = 1;
		}
		m[n + 1] = d;
		//반대 방향으로 회전
		dfs_right(n + 1, d);
	}
}


int main() {
	string s;

	for (int i = 0; i < 4; i++) {
		cin >> s;
		for (int j = 0; j < s.size(); j++) {
			v[i].push_back(s[j]-48);
		}
	}
	int k;
	cin >> k;
	int n, d;
	for (int i = 0; i < k; i++) {
		cin >> n >> d;
		n--;
		m[n] = d;
		dfs_left(n, d);
		dfs_right(n, d);
		for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
			rotate(it->first, it->second);
		}
		m.clear();
	}

	int ans = 0;
	for (int i = 0; i < 4; i++) {
		if (v[i][0] == 1) {
		
			ans += pow(2,i);
		}
	}

	
	cout << ans;
}