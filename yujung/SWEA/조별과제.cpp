#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
 
int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		int ans = n / 3;

		cout << "#" << t << " " << ans<<"\n";
	}
}