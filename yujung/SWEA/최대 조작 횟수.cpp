#include<iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long answer = 0; //10^18이니까 long long 타입
		long long a, b;
		cin >> a >> b;
		if (abs(a - b) <= 1) {
			if (a == b) {
				answer = 0;
			}
			else {
				answer = -1;
			}

		}
		else if (a > b) { //A는 더하고, B는 빼기 밖에 못함
			answer = -1;
		}
		else {
			answer = abs(a - b) / 2;
		}
		cout << "#" << t << " " << answer << "\n";
	}
}