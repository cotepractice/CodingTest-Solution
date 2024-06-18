#include<iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int T, N, x, y, score, i, d, d2;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		score = 0;
		cin >> N;
		for (i = 0; i < N; i++) {
			cin >> x >> y;
			d2 = x * x + y * y;

			for (d = 20; d <= 200; d += 20)
				if (d*d >= d2)
					break;
			score += 11 - d / 20;
		}
		cout << '#' << t<< ' ' << score << '\n';
	}
	return 0;
}