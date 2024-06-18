#include <iostream>
#include <vector>
#include <algorithm>
#include<string>
using namespace std;

int main() {
	
	int T;
	
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int N, M, K;
		cin >> N >> M >> K;
		vector<int> arrive_time(N);
		for (int i = 0; i < N; i++) {
			cin>> arrive_time[i];
		}
		sort(arrive_time.begin(), arrive_time.end());

		string result = "Possible";
		for (int i = 0; i < N; i++) {
			int boong = (arrive_time[i] / M) * K - (i + 1);
			if (boong < 0) {
				result = "Impossible";
				break;
			}
		}
		cout << "#" << tc << " " << result << endl;
	}

	return 0;
}