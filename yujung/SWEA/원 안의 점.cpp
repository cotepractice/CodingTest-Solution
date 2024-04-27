#include<iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		int cnt = 0;
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= n; j++) {
				if (i*i + j * j <= n * n) {
					cnt++;
				}
			}
		}
		cnt = (cnt - (n + 1)) * 4 + 1;
		
		cout <<"#"<<t<<" "<<cnt<<"\n";
	}
	
}