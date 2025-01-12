#include<iostream>
#include<algorithm>
using namespace std;
#define MAX_N 13
int day, month, three_month, year;
int plan[MAX_N];
int dp[MAX_N];
//11,12
int main() {
	int T; 
	cin >> T;
	for (int t = 1; t <= T; t++) {

		cin >> day >> month >> three_month >> year;
		for (int i = 1; i <= 12; i++)
		{
			cin >> plan[i];
		}

		dp[1] = min(plan[1] * day, month);
		dp[2] = min(dp[1] + plan[2] * day, dp[1] + month);

		for (int i = 3; i <= 12; i++)
		{
			dp[i] = min({ dp[i - 1] + plan[i] * day , dp[i - 1] + month, dp[i - 3]+three_month });
		}

		if (dp[12] > year) {
			dp[12] = year;
		}
		cout <<"#"<<t<<" "<< dp[12]<<"\n";

		for (int i = 0; i <= 12; i++) {
			dp[i] = 0;
		}
	}

	
}