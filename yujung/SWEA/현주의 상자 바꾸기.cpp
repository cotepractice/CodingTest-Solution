#include <iostream>
#include <vector>
#include <algorithm>
#include<cstring>

using namespace std;

int main() {
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, q;
		cin >> n >> q; //상자의 개수, q회 동안 일정 번위의 연속한 상자를 동일
		int arr[1001];
		memset(arr, 0, sizeof(arr));
		for (int i = 1; i <= q; i++) { //i번째
			int a,b;
			cin >> a >> b;
			for (int j = a; j <= b; j++) {
				arr[j] = i;
			}
		}


		
		cout << "#" << t << " ";

		for (int i = 1; i <= n; i++) {
			cout << arr[i] << " ";
		}
		cout << "\n";
	}
	


	return 0;
}