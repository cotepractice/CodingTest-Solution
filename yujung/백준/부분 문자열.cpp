#include<iostream>
#include<string>
#include<cstring>

using namespace std;
string s;
string p;
int main() {

	cin >> s;
	cin >> p;
	char *ptr = strstr((char*)s.c_str(), (char*)p.c_str());
	if ( ptr== NULL) {
		cout << 0;
	}
	else {
		cout << 1;
	}
	
}