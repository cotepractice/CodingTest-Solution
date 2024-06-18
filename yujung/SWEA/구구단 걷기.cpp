#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;



int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long n;
		cin >> n;
		long long answer = n-1;
		for (int i = 1; i <= sqrt(n); i++) {
			if (n % i == 0) {
				long long a = n / i;
				 long long b = i;
			
				answer = min(answer, (a - 1) + (b - 1));
			
			};
		}
		cout <<"#"<<t<<" "<< answer<<"\n";
	}
	
}