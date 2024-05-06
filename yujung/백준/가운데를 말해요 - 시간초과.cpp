#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
vector<int> v;
vector<int> ans;
int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
		sort(v.begin(), v.end());
		if (i % 2 == 1) {//홀수이면

			cout << v[i / 2] << "\n";
		}
		else {
			if (v[i / 2 - 1] > v[i / 2]) {
				cout << v[i / 2]<<"\n";
			}
			else {
				cout << v[i / 2-1]<<"\n";
			}
		}
	}
}