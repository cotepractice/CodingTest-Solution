#include<iostream>
using namespace std;
#define MAX_N 500

int n;
int map[MAX_N][MAX_N];
//동

int dir[4][10][2] = {
	{{-1,1}, {1,1},{-1,0},{1,0},{-2,0},{2,0},{-1,-1},{1,-1}
	,{0,-2},{0,-1}},
{ {-1,-1},{-1,1}, {0,-1},{0,1},{0,-2},{0,2},{1,-1},{1,1},{2,0},{1,0} }
,{ {-1,-1},{1,-1},{-1,0 } ,{1,0},{-2,0},{2,0},{-1,1},{1,1},{0,2},{0,1} }
,{ {1,-1},{1,1}, {0,-1},{0,1},{0,-2},{0,2},{-1,-1},{-1,1},{-2,0},{-1,0} }
};


int per[9] = { 1,1,7,7,2,2,10,10,5 };

int dx[4] = { 0,1,0,-1 }; //서, 남, 동, 북
int dy[4] = { -1,0,1,0 };

int cnt = 0;
int small = 0;
int large = 1;
int direc = 0;
int rr;
int rc;
int ex = 0;
bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < n&&y < n;
}
void morae() {
	int curr = map[rr][rc];
	map[rr][rc] = 0;
	int sum = 0;
	for (int i = 0; i < 9; i++)
	{
		int p = per[i];
		int a = (curr*p) / 100;
		int rx = dir[direc][i][0];
		int ry = dir[direc][i][1];
		int nx = rr + rx;
		int ny = rc + ry;
		sum += a;
		if (!is_range(nx, ny)) {
			ex += a;
			continue;
		}
		map[nx][ny] += a;

	}

	int rx = dir[direc][9][0];
	int ry = dir[direc][9][1];
	int nx = rr + rx;
	int ny = rc + ry;
	if (!is_range(nx, ny)) {
		ex += (curr - sum);
		return;
	}
	map[nx][ny] += (curr - sum);
}
void rotate() {
	cnt++;

	rr += dx[direc];
	rc += dy[direc];

	morae();

	if (cnt == large) {
		direc = (direc + 1) % 4;
		small++;
		cnt = 0;
	}
	if (small == 2) {
		large++;
		small = 0;
	}
}
int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> map[i][j];
		}
	}
	rr = n / 2;
	rc = n / 2;

	while (1) {
		rotate();
		if (rr == 0 && rc == 0)
		{
			break;
		}
	}
	cout << ex;
}