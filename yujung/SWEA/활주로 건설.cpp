#include<iostream>
#define MAX_N 51
using namespace std;

int N, X;
int map[MAX_N][MAX_N];
bool visited[MAX_N];
int cnt = 0;
bool is_range(int x)
{
	return x >= 0 && x < N;
}

void init() {
	for (int i = 0; i < N; i++) {
		visited[i] = false;
	}
}
void func() {
	for (int i = 0; i < N; i++) {
		bool f = true;
		init();
		for (int j = 0; j < N - 1; j++) {
			if (map[i][j] != map[i][j + 1]) {


				if (map[i][j] < map[i][j + 1]) {
					if (abs(map[i][j + 1] - map[i][j]) >= 2) { f = false; break; };
					for (int k = j - X + 1; k <= j; k++) {
						if (!is_range(k) || visited[k] == true) { f = false; break; }

						if (map[i][k] != map[i][j + 1] - 1) { f = false; break; }
						visited[k] = true;
					}
				}
				else {
					if (abs(map[i][j + 1] - map[i][j]) >= 2) { f = false; break; };
					for (int k = j + 1; k <= j + X; k++) {
						if (!is_range(k) || visited[k] == true) { f = false; break; }

						if (map[i][k] != map[i][j] - 1) { f = false; break; }
						visited[k] = true;
					}
					j+=X-1;
				}

			}
		}
		if (f == true)cnt++;
	}
}

void func2() {
	for (int i = 0; i < N; i++) { //열
		bool f = true;
		init();
		for (int j = 0; j < N - 1; j++) { //행
			if (map[j][i] != map[j + 1][i]) {


				if (map[j][i] < map[j + 1][i]) {
					if (abs(map[j+1][i] - map[j][i]) >= 2) { f = false; break; };

					for (int k = j - X + 1; k <= j; k++) {
						if (!is_range(k) || visited[k] == true) { f = false; break; }

						if (map[k][i] != map[j + 1][i] - 1) { f = false; break; }
						visited[k] = true;
					}
				}
				else {
					if (abs(map[j + 1][i] - map[j][i]) >= 2) { f = false; break; };
					for (int k = j + 1; k <= j + X; k++) {
						if (!is_range(k) || visited[k] == true) { f = false; break; }

						if (map[k][i] != map[j][i] - 1) { f = false; break; }
						visited[k] = true;
					}
					j+=X-1;
				}

			}
		}
		if (f == true)cnt++;
	}
}
int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cnt = 0;
		cin >> N >> X;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> map[i][j];
			}
		}

		func();
		func2();
		cout << "#" << t << " " << cnt << endl;
	}



}