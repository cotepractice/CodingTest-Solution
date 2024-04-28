#include<iostream>
#include<algorithm>
#include <iomanip>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int a, b, c;
		cin >> a;
		cin >> b;
		cin >> c;
		//1,2,1
		//오름차순

		float tmp1;
		float tmp3;
		if (c > b) { //5   3 9
			
			tmp1 = abs(a - (b - abs(b - c)));
		}
		else if (c == b) {
			tmp1 = abs(b - a);
		}
		else {//  9 3
			
			tmp1 = abs(a - (b + abs(b - c)));
		}//a를 바꾸는 경우

		float tmp2 = abs(float(a + c) / 2 - b);
	
		if (a < b) { //1 4
			tmp3 = abs(c - (b + abs(a - b)));
		}
		else if (a == b) {
			tmp3 = abs(b - c);
		}
		else {  

			tmp3 = abs(c - (b - abs(a - b)));
		}
	//	cout << tmp1 << tmp2 << tmp3 << "\n";
	

		float answer = min(tmp1, min(tmp2, tmp3));
		if (answer == 0||(a==b&&b==c&&a==c)) {
			cout << fixed << setprecision(1)<<"#" << t << " " << float(0) << "\n";
		}
		else {
			cout << fixed << setprecision(1) << "#" << t << " " << answer << "\n";
		}
		

	}

	
	
}