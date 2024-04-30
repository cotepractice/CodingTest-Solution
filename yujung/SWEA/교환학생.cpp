#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
 
// 1 1 0 0 1 1 0인 경우 최소 4인데 5로 잘못 출력됨 
int main() {
	int T;
	cin >> T;
	int answer = 0;
	int arr[7];
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
	
		for (int i = 0; i < 7; i++)
		{
			cin>>arr[i];
		}
		int res = 1000000;
		for (int i = 0; i < 7; i++) {
			if (arr[i] == 1) {
				int idx = i;
				int tmp = n;
				int ans = 0;
				while (tmp != 0) {
					if (arr[idx] == 1) {
						tmp--;

					}
					ans++;
					idx = (idx + 1) % 7;
				}
				res = min(ans, res);
			}
			
		}
		cout << "#" << t << " " << res<<"\n";
	}

	
}