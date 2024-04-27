#include<iostream>
#include<string>
using namespace std;
string s;

bool func(string s) {
	if (s.size() % 2 == 1) {//홀수이면
		int n = (s.size() - 1) / 2;
		for (int i = 0; i < n; i++) {
			if (s[i] != s[s.size() - 1 - i]) {
				//회문이 아님
				return false;
			}
		}
	}
	else {//짝수이면
		//회문이 아님
		int n = (s.size())/2;
		for (int i = 0; i < n; i++) {
			if (s[i] != s[s.size() - 1 - i]) {
				//회문이 아님
				return false;
			}
		}
	
	}
	return true;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> s;
		if (func(s) && func(s.substr(0, s.size() / 2))) {
			cout <<"#"<<t<<" "<<"YES" << "\n";
		}
		else {
			cout << "#" << t << " " << "NO" << "\n";
		}
	}
	
}