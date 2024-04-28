#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<string> s;
int cnt = 0;
bool f = false;
int n;
bool check() {
	cnt = 0;
	for (int i = 0; i < 8; i++) {
		string a;
		cin >> a;
		s.push_back(a);
		for (int j = 0; j < 8; j++) {
			if (a[j] == 'O') {
				cnt++;
			}
		}
	}
	if (cnt != 8)return true;
	int cnt2;
	for (int i = 0; i < 8; i++) {
		cnt2 = 0;
		for (int j = 0; j < 8; j++) {
			if (s[i][j] == 'O')cnt2++;
			if (cnt2 >= 2) {
				return true;
			}
		}
		if (cnt2 >= 2 || cnt2 == 0) { return true; }
	}


	for (int i = 0; i < 8; i++) {
		cnt2 = 0;
		for (int j = 0; j < 8; j++) {
			if (s[j][i] == 'O')cnt2++;
			if (cnt2 >= 2) {
				return true;
			}
		}
		if (cnt2 >= 2 || cnt2 == 0) { return true; }
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		if (check() == true) {
			cout <<"#"<<t<<" "<< "no"<<"\n";
		}
		else {
			cout <<"#"<<t<<" "<<"yes"<<"\n";
		}
		s.clear();
	}
	

	
}