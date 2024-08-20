#include<iostream>
#include<string>
using namespace std;

int main() {
	string al = "abcdefghijklmnopqrstuvwxyz";
	string s;
	cin >> s;
	for (int i = 0; i < al.size(); i++) {
			cout <<(int)s.find(al[i])<<" ";
	}
}