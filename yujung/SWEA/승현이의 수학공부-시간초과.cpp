#include<iostream>
#include<map>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

int arr[1001];
int recursive(int a,int n)
{
	int sum = 1;
	for (int i = 0; i < n; i++) {
		sum *= a;
	}
	return sum;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		string x;
		cin >> n >> x;
		int sum = 0;
		int first = x.size() - 1;
		for (int i = 0; i < x.size(); i++) {
		
			sum+=recursive(n, first)*x[i] - '0';
			first--;
		}
		sum %= (n - 1);
		cout << "#"<<t<<" "<<sum<<"\n";
	}
	


}