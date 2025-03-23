#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
#define MAX_N 10

int n, m, r;
int map[MAX_N][MAX_N];
int tmp[MAX_N][MAX_N];

void rotate(int num) {

	if (num == 1)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				tmp[n-1-i][j] = map[i][j];
			}
		}
		
	}

	if (num == 2)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				tmp[i][m-1-j] = map[i][j];
			}
		}

	}

	if (num == 3)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				int x = i - n;
				int y = j - m;
				int cx = y + m;
				int cy = x + n;
				tmp[cx][n - 1 - cy] = map[i][j];
			}
		}

	}

	if (num == 4)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				int x = i - n;
				int y = j - n;
				int cx = y + m;
				int cy = x + n;
				tmp[m-1-cx][cy] = map[i][j];
			}
		}
		int tmp = n;
		n = m;
		m = tmp;

	}
	if (num == 5)
	{
		int nx = n / 2;
		int my = m / 2;
		for (int i = 0; i < nx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				tmp[i][my+j] = map[i][j];
			}
		}
		for (int i = 0; i < nx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				tmp[nx+i][j] = map[i][j];
			}
		}
		for (int i = nx; i < n; i++)
		{
			for (int j = my; j < m; j++)
			{
				tmp[i][j-my] = map[i][j];
			}
		}
		for (int i = nx; i < n; i++)
		{
			for (int j = 0; j < my; j++)
			{
				tmp[i-nx][j] = map[i][j];
			}
		}
	}

	if (num == 6)
	{
		int nx = n / 2;
		int my = m / 2;
		for (int i = 0; i < nx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				tmp[nx+i][my + j] = map[i][j];
			}
		}
		
		for (int i = nx; i < n; i++)
		{
			for (int j = 0; j < my; j++)
			{
				tmp[i][j - my] = map[i][j];
			}
		}

		for (int i = nx; i < n; i++)
		{
			for (int j = 0; j < my; j++)
			{
				tmp[nx + i][j+my] = map[i][j];
			}
		}
		for (int i = nx; i < n; i++)
		{
			for (int j = my; j < m; j++)
			{
				tmp[i - nx][j] = map[i][j];
			}
		}
	}


}
int main() {
	cin >> n >> m >> r;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}
	rotate(5);


}