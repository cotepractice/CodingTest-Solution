#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool arr[101][101][2];
int arrSize;

bool check(int x, int y) {
	if (x < 0 || y < 0 || x > arrSize || y > arrSize) {
		return false;
	}
	return true;
}

bool isSetPossible(int x, int y, int type) {
	if (type == 0) {
		if (y == 0) return true;
		if ((check(x - 1, y) && arr[x - 1][y][1]) || arr[x][y][1])
			return true;
		if (check(x, y - 1) && arr[x][y - 1][0])
			return true;
	}

	else {
		if ((check(x, y - 1) && arr[x][y - 1][0]) || (check(x + 1, y - 1) && arr[x + 1][y - 1][0]))
			return true;
		if ((check(x - 1, y) && check(x + 1, y)) && arr[x - 1][y][1] && arr[x + 1][y][1])
			return true;
	}

	return false;
}

bool isRemovePossible() {
	for (int x = 0; x <= arrSize; x++) {
		for (int y = 0; y <= arrSize; y++) {
			for (int i = 0; i < 2; i++) {
				if (arr[x][y][i]) {
					arr[x][y][i] = false;
					if (!isSetPossible(x, y, i)) {
						arr[x][y][i] = true;
						return false;
					}
					arr[x][y][i] = true;
				}
			}
		}
	}
	return true;
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame) {
	vector<vector<int>> answer;
	arrSize = n;

	for (int i = 0; i < build_frame.size(); i++) {
		int x, y, a, b;
		x = build_frame[i][0];
		y = build_frame[i][1];
		a = build_frame[i][2];
		b = build_frame[i][3];

		if (a == 0) {
			if (b == 1) {
				if (isSetPossible(x, y, 0)) {
					arr[x][y][0] = true;
				}
			}

			else if (b == 0) {
				arr[x][y][0] = 0;
				if (!isRemovePossible()) {
					arr[x][y][0] = true;
				}
			}
		}
		else if (a == 1) {
			if (b == 1) {
				if (isSetPossible(x, y, 1)) {
					arr[x][y][1] = true;
				}
			}
			// 삭제일 때
			else if (b == 0) {
				arr[x][y][1] = false;

				if (!isRemovePossible()) {
					arr[x][y][1] = true;
				}
			}
		}
	}

	for (int x = 0; x <= arrSize; x++) {
		for (int y = 0; y <= arrSize; y++) {
			for (int i = 0; i < 2; i++) {
				if (arr[x][y][i]) {
					vector<int> tmp;
					tmp.push_back(x);
					tmp.push_back(y);
					tmp.push_back(i);

					answer.push_back(tmp);
				}
			}
		}
	}

	return answer;
}