#include <iostream>
#include <stack>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
	
		string ans = "";
		map<char, int> m;
		string s;
		cin >> s;


		/*for (int i = 0; i < s.size(); i++) {
			m[s[i]] = 0;
		}*/
		for (int i = 0; i < s.size(); i++) {
			m[s[i]]++;
		}
		for (int i = 0; i < s.size(); i++) {
			if (m[s[i]] % 2 == 1) {
				m[s[i]] = 1;
			}
			else {
				m[s[i]] = 0;
			}
		}
		cout << "#" << t << " ";
		int f = false;
		for (int i = 0; i < s.size(); i++) {
			while (m[s[i]] > 0) {
				ans+=s[i];
				m[s[i]]--;
				f = true;
			}
		}
		sort(ans.begin(), ans.end());
		if (f == false) {
			cout << "Good";
		}
		else {
			cout << ans;
		}
		cout << "\n";
	}
	

	
	
}