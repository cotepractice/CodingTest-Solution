#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int tc = 0; tc < T; tc++) {
		int N;
		cin >> N;
		int num1 = N * 9;
		int num2 = N * 8;
		cout << "#" << tc + 1 << " " << num1 << " " << num2 << endl;
	}

	return 0;
}