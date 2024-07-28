#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
	string s;
	while (1) {
		getline(cin, s);
		if (s == "END") {
			break;
		}
		reverse(s.begin(), s.end());
		cout <<s<< endl;
	}
	
}