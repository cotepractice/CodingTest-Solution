#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
 
// 1 1 0 0 1 1 0인 경우 최소 4인데 5로 잘못 출력됨 
int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		int arr[7];
		for (int i = 0; i < 7; i++) {
			cin >> arr[i];
		}
		int answer = 0;
		int first_idx = -1;
		int cnt = 0;
		int max_cnt = 0;
		int max_idx;
		for (int i = 0; i < 2; i++) {
			for (int i = 0; i < 7; i++) {

				if (arr[i] == 1) {
					cnt++;
				}
				else {
					cnt = 0;
				}

				if (cnt > max_cnt) {
					max_cnt = cnt;
					max_idx = i;
				}
			}
		}
		
		first_idx = max_idx - (max_cnt - 1);
		if(max_idx - (max_cnt - 1) < 0) {
			first_idx += 7;
		}
		
		cout << first_idx;
	
		bool f = false;
		while(true) {
		//	cout << n<<endl;
			for (int i = 0; i < 7; i++) {
				if (f == false) {
					f = true;
					i=first_idx;
				}
				answer++;
				if (arr[i] == 1) {
					n--;
					//cout << n;
				}
				if (n == 0) {
					break;
				}
			}
			if (n == 0) {
				break;
			}
		}
		

		cout << "#" << t << " " << answer<<"\n";
	}

	
}