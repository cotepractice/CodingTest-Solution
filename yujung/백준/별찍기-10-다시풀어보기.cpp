#include<iostream>
using namespace std;

void star(int i, int j, int num) {
	if ((i/num )%3 == 1 && (j /num)%3 == 1) {
		cout << " ";
	}
	else
	{
		if (num / 3 == 0) {
			cout << "*";
		}
		else {
			star(i, j, num / 3);
		}
	}
}
int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			star(i, j, n);
		}
		cout << "\n";
	}
}