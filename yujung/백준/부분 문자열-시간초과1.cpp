#include<iostream>
#include<string>
using namespace std;

int main() {
	string s;
	string p;
	cin >> s;
	cin >> p;
	int answer = 0;
	for (int i = 0; i < s.size()-p.size()+1; i++) {
		if (s.substr(i, p.size()) == p) {
			answer = 1;
			break;
		}
	}
	cout << answer;
}