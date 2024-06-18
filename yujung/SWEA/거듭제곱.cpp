#include<iostream>
using namespace std;

int n, m;
long long res = 1;
void recursive(int cnt) {
	if (cnt == m) { return; }
	res *= n;
	recursive(cnt + 1);
}
int main() {
	
	for (int t = 1; t <= 10; t++) {
		int a;
		cin >> a;
		res = 1;
		cin >> n >> m;
		recursive(0);
		cout << "#"<<t<<" "<<res<<"\n";
	}
	

}