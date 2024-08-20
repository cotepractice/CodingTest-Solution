#include<iostream>
#include<string>
using namespace std;

int main() {
	string alpha ;
	int res = 0;
	cin >> alpha;
	for (int i = 0; i < alpha.size(); i++) {
		int cnt=alpha[i] - 'A';
//V가 
	//	cout << cnt<<" ";
			if (cnt == 18) {
				res += cnt / 3 + 2;
			}
			else if (cnt == 21) {
				res += cnt / 3 + 2;
			}
			else if (cnt == 24 || cnt==25) {
				res += cnt / 3 + 2;
			}
			else {
				res += cnt / 3 + 3;
			}
	//		cout << res << "\n";
			
	}
	cout << res;
	

	
	

}