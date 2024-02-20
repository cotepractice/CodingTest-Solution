#include<iostream>
#include<vector>

using namespace std;

vector<int> v ;
void go(int st, int en) {
	if (st >= en) { return; }
	if (st == en - 1) { cout << v[st] << endl; return; }
	int idx = st + 1;
	while (idx < en) {
		if (v[st] < v[idx])break;
		idx++;
	}
	go(st + 1, idx);
	go(idx, en);
	cout << v[st] << endl;
	return;
}
int main() {
	int n;
	while (cin >> n) {
		v.push_back(n);
	}
	go(0, v.size());
}