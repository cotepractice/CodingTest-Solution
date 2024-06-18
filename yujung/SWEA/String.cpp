#include<iostream>
#include<string>
using namespace std;


int main() {
	
	for (int t = 1; t <= 10; t++) {
		int dumi;
		cin >> dumi;
		string s1;
		string s2;
		int ans = 0;

		cin >> s1 >> s2;
		for (int i = 0; i < s2.size(); i++) {
			int tmp = 0;
			while (s1[tmp] == s2[i + tmp]) {
				tmp++;
				if (tmp == s1.size()) {
					ans++;
				}
			}
		}
		cout <<"#"<<t<<" "<< ans<<"\n";
	}
	
}