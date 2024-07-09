#include<iostream>
#include<string>
using namespace std;

//'a'는 97
//'A'는 65

int main() {
	string key ;
	string s;
	string ans;
	getline(cin, s);
	cin >> key;
	int idx=0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == ' ')ans += ' ';
		else if (s[i] - key[idx] <= 0) {
			ans += s[i] - key[idx] + 'a' +26-1;
		}
		else {
			ans += s[i] - key[idx] + 'a'-1;
		}
		idx = (idx + 1) % key.size();
	}

	cout <<ans;
}