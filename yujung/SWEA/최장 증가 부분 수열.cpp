#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int TC;
	cin >> TC;

	for (int t = 1; t <= TC; ++t) {
		int N;
		cin >> N;
		vector<int> arr(N);
		
		for (int i = 0; i < N; ++i) {
			cin >> arr[i];
		}
		vector<int> dp(N, 1);

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < i; ++j) {
				if (arr[i] > arr[j]) {
					dp[i] = max(dp[i], dp[j] + 1);
				}
			}
		}
		sort(dp.begin(), dp.end());
		
		cout << "#" << t << ' ' << dp[dp.size() - 1] << "\n";
	}
}