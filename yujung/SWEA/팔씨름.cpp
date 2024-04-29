#include<iostream>
#include<string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string answer = "YES";
		string s;
		cin >> s;
		//15->8
		int cnt = 0;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == 'o') {
				cnt++;
			}
		}
		int win = 15 - s.size();
		win += cnt;
		if (win < 8) {
			answer = "NO";
		}
		cout << "#" << t<<" " << answer << "\n";
	}
	
}