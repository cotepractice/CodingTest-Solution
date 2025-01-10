#include <iostream>

using namespace std;

int p[128][128];
int white = 0, blue = 0;

void solved(int x, int y, int size) {

	int check = p[x][y];
	for (int i = x; i < x + size; i++) {
		for (int j = y; j < y + size; j++) {
			if (check == 0 && p[i][j] == 1) {
				check = 2;
			}
			else if (check == 1 && p[i][j] == 0) {
				check = 2;
				
			}
			if (check == 2) {
				solved(x, y, size / 2);
				solved(x, y + size / 2, size / 2);
				solved(x + size / 2, y, size / 2);
				solved(x + size / 2, y + size / 2, size / 2);
				return;
}
		}
	}
	if (check == 0) {
		white++;
	}
	else if (check == 1) {
		blue++;
	}
}
int main()
{
	int size;
	cin >> size;
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++)
		{
			cin >> p[i][j];
		}
	}
	solved(0, 0, size);
	cout << white << endl << blue << endl;
}
//white blue가 