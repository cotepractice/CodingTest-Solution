#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> arr;
vector<int> ans;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		for (int i = 0; i < n * 2; i++) {
			int a;
			cin >> a;
			arr.push_back(a);
		}
		for (int i = n * 2 - 1; i >= 1; i--) {
			for (int j = i - 1; j >= 0; j--) {
				//cout << (int)(arr[i] * 0.75) << " ";
				if ((int)(arr[i] * 0.75) == arr[j]) {

					ans.push_back(arr[j]);
					arr.erase(arr.begin() + i);
					arr.erase(arr.begin() + j);
					i -= 1;
					break;

				}

			}


		}
		sort(ans.begin(), ans.end());
		cout << "#" << t << " ";
		for (auto a : ans) {
			cout << a << " ";
		}
		cout << "\n";
		ans.clear();
	}
	
}