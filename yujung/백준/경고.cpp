#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int htos(int h, int m,int s) {
	return h * 3600 + m * 60 + s;
}
vector<int> func(int time) {
	int s=time % 60;
	int m=time % 3600 /60;
	int h = time / 3600 ;
	vector<int> a = { h,m,s };
	return a;
}
int main() {
	string a;
	string b;
	cin >> a;
	cin >> b;
	int first=htos(stoi(a.substr(0, 2)), stoi(a.substr(3, 2)), stoi(a.substr(6,2)));
	int second = htos(stoi(b.substr(0, 2)), stoi(b.substr(3, 2)), stoi(b.substr(6, 2)));
	if (first == second) {
		cout << "24:00:00";
		return 0;
	}
	if (first > second) {
		second += 24 * 3600;
	}
	int res=second - first;
	vector<int> v=func(res);
	string ans;
	if (v[0] < 10) {
		ans += "0";
	}
	ans += to_string(v[0]);
	ans += ":";

	if (v[1] < 10) {
		ans += "0";
	}
	ans += to_string(v[1]);
	ans += ":";

	if (v[2] < 10) {
		ans += "0";
	}
	ans += to_string(v[2]);
	cout << ans;
}