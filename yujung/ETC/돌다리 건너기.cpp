#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main() {
	int dp[45];
	 dp[1] = 1;
	 dp[2] = 2;
	 int n;
	 cin >> n;
	 for (int i = 3; i <= n+1; i++) {
		 dp[i] = dp[i - 2]+ dp[i - 1];
	 }
	 cout << dp[n+1];

}