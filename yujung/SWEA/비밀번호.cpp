#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {
	
	for (int t = 1; t <= 10; t++) {
		int n;
		cin >> n;
		string s;
		cin >> s;
		while (true) {
			bool f = false;
			for (int i = 0; i < s.size() - 1; i++) {//s사이즈가 있잖아
				if (s[i] == s[i + 1]) {
					f = true;
					s.erase(s.begin() + i);
					s.erase(s.begin() + i);
				}
			}
			if (f == false) {
				break;
			}
		}
		cout << "#"<<t<<" "<<s<<"\n";
	}
	

}