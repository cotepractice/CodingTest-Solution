#include<iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, m;
		cin >> n >> m;
		int x = (1 << n) - 1;
		if ((m&x)==x) {
			cout << "#" << t << " ON" << endl;
		}
		else {
			cout << "#" << t << " OFF" << endl;
		}
	}
	
}