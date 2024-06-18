#include<iostream>
#include<map>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

int arr[1001];
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		int res = -1;
		for (int i = 0; i < n-1; i++) {
			for (int j = i; j < n; j++) {
				int sum = arr[i] + arr[j];
				if (sum > res && m>=sum ){
					res = max(sum,res);
				}
			}
		}
		cout << "#"<<t<<" "<<res<<"\n";
	}
	


}