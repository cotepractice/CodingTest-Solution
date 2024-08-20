#include<iostream>
#include<string>
using namespace std;

int main() {
	int a;
	string b;
	cin >> a;
	cin >> b;

	int res=0;
	for (int i = 0; i < b.size(); i++) {
		res += b[i]-'0';
	}
	cout << res;
}