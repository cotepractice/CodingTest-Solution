#include<iostream>
using namespace std;

int arr[3];
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < 3; i++) {
			cin >> arr[i];
		}
		int answer = 0;
		if (arr[2] < 3 or arr[1] < 2) { cout << "#" << t << " " << -1 << "\n";}
		else {
			for (int i = 2; i >= 1; i--) {

				if (arr[i] <= arr[i - 1]) {
					int a = arr[i - 1] - (arr[i] - 1);
					answer += a;
					arr[i - 1] = arr[i] - 1;
				}
			}
			cout << "#" << t << " " << answer << "\n";
		}
		
	}
	
}