#include <iostream>
#include <string>
using namespace std;

int test_case, T, j, cnt;
string str;

int main() {
	cin >> T;

	for (test_case = 1; test_case <= T; test_case++) {
		cin >> str;
		cnt = 0;

		for (int i = 0; i < str.size() - 1; i++) {
			if (str.substr(i, 2) == "(|" || str.substr(i, 2) == "|)" || str.substr(i, 2) == "()")
				cnt++;
		}

		cout << "#" << test_case << " " << cnt << "\n";
	}
}