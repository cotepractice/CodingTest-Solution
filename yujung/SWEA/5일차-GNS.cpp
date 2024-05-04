#include<iostream>
#include<map>
#include<cstring>
#include<string>
using namespace std;


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		map<string, int>m;
		string arr[10] = { "ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN" };
		int count[10];
		memset(count, 0, sizeof(count));
		for (int i = 0; i < 10; i++) {
			m[arr[i]] = i;
		}

		char c;
		cin >> c;
		int b;
		cin >> b;

		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			string a;
			cin >> a;
			count[m[a]] += 1;
		}

		cout << "#" << t << " ";
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < count[i]; j++) {
				cout << arr[i] << " ";
			}
		}
		cout << "\n";
	}
	


}