#include<iostream>
#include<map>
#include<algorithm>
#include<string>
using namespace std;
map<char, int> m;
int main() {
	int n;
	cin >> n;
	cin.ignore();
	while (n--){
		string s;
		getline(cin, s);
		for (int i = 0; i < s.size(); i++) {
			if (isalpha(s[i])) {
				m[s[i]]++;
			}
		}
		int res = 0;
		char c;
		for (auto a : m) {
			if (res < a.second) {
				res = a.second;
				c = a.first;
			}
		}
		int cnt = 0;
		for (auto a : m) {
			if (res == a.second) {
				cnt++;
			}
			if (cnt >= 2) {
				c = '?';
				break;
			}
		}
		cout << c << endl;
		m.clear();
	}
	
}