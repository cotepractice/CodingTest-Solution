#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int a, b;
		cin >> a >> b;
		int answer = 0;
		if (a % (b * 2 + 1) == 0) {
			 answer = a / (b * 2 + 1);
		}
		else {
			answer = a / (b * 2 + 1)+1;
		}
		cout << "#" << t << " " << answer << "\n";
	}

	
}