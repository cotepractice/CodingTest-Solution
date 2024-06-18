#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string n;
		cin >> n;
		string f = "impossible";

		int cnt = 2;
		while (true) {
			string s = to_string(stoi(n) * cnt);
			cnt++;
			if (s.size() != n.size()) {
				break;
			}
			set<char> c1(n.begin(),n.end());
			set<char> c2(s.begin(),s.end());
			if (c1 == c2) {
				f = "possible";
				break;
			}
		}
		cout << "#" << t << " " << f << "\n";
	}

	
}