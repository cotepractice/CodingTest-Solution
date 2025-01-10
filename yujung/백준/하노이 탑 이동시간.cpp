#include<iostream>
using namespace std;
int n;

void hanoi(int n, int start, int dest) {
	if (n == 1)
	{
		cout << start << " " << dest << '\n';
		return;
	}
	hanoi( n - 1, start, 6 - start - dest);
	cout << start << " " << dest << '\n';
	hanoi( n - 1, 6 - start - dest, dest);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	cout << (1 << n) - 1<<endl;
	hanoi(n, 1, 3);

}