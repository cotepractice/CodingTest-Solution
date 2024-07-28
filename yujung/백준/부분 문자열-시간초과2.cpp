#include<iostream>
#include<string>
#include<cstring>

using namespace std;
string s;
string p;
int main() {

	cin >> s;
	cin >> p;
	if (s.find(p) != string::npos) {
		cout << 1 << "\n";
	}
	else {
		cout << 0 << "\n";
	}
	
	
}