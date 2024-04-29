#include<iostream>
using namespace std;

int map[101];
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long a, b, c, d;
		long long cnt = 0;
		cin >> a >> b >> c >> d;
		for (int i = a; i <= b; i++) {
			map[i]++;
		}
		for (int i = c; i <= d; i++) {
			map[i]++;
			if (map[i] == 2) {
				cnt++;
			}
		}
		if (cnt != 0) {
			cnt--;
		}
		cout <<"#"<<t<<" "<< cnt<<"\n";
	}
	

}