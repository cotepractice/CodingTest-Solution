#include<iostream>
using namespace std;

int a, b;

int gcd(int a, int b) {
	if (a%b == 0) {
		return b;
	}
	return gcd(b, a%b);
}
int main() {
	cin >> a >> b;
	cout << gcd(a, b)<<"\n";
	cout << a * b / gcd(a, b);
}