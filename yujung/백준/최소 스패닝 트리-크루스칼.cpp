#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int parent[10001];
int sum = 0;
int find(int x) {
	if (parent[x] == x) return x;
	return parent[x]=find(parent[x]);
}

void uni(int x, int y) {
	x = find(x);
	y = find(y);
	parent[y] = x;
}

bool same(int x, int y) {
	x = find(x);
	y = find(y);
	if (x == y) return true;
	return false;
}
int main() {
	int a, b;
	cin >> a >> b;
	vector < pair<int, pair<int, int>>> v;
	for (int i = 0; i < b; i++) {
		int m1, m2, m3;
		cin >> m1 >> m2 >> m3;
		v.push_back(make_pair(m3, make_pair(m1,m2)));
	}
	sort(v.begin(), v.end());
	for (int i = 1; i < a + 1; i++) {
		parent[i] = i;
	}

	for (int i = 0; i < v.size(); i++) {
		if (!same(v[i].second.first, v[i].second.second))
		{
			uni(v[i].second.first, v[i].second.second);
			sum+=v[i].first;
		}
	}
	cout << sum;
}