#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
 
int main() {
	int T;
	cin >> T;
	string arr[7] = { "MON","TUE","WED","THU","FRI","SAT","SUN" };
	int a[7] = { 6,5,4,3,2,1,7 };
	int ans;
	for (int t = 1; t <= T; t++) {
		string num;
		
		cin >> num;
		for (int i = 0; i < 7; i++) {
			if (num == arr[i]) {
				ans = a[i];
				break;
			}

		}
		cout << "#" << t << " " << ans<<"\n";
	}
}