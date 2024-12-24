#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int n;
long long ans = 0;
vector<int> v;
int x, y;

int main() {
	cin >> n;
	ans += n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	cin >> x >> y;
	for (int i = 0; i < n; i++) {
		v[i] -= x;
		if (v[i] > 0) {
		   ans+=(v[i] + y - 1)/ y;
		}
	}
	
	cout << ans;
}