#include<iostream>
#include<vector>
#include<string>
using namespace std;

char arr[20][20];

int dx[4] = { 0,0,1,-1 }; //오,왼,아래,위
int dy[4] = { 1,-1,0,0 };
//. 평지, * 벽돌, # 강철, - 물
int sx, sy;
int n, m;
int dir = -1;
bool is_range(int x,int y) {
	return (x >= 0 && y >= 0 && x < n&&y < m);
}
void func(char s) {
	if (s == 'S') {
		int nx = sx;
		int ny = sy;
		while (true) {
			nx += dx[dir];
			ny += dy[dir];
			if (!is_range(nx, ny))break;
			if (arr[nx][ny] == '#')break;
			if (arr[nx][ny] == '*') {
				arr[nx][ny] = '.';
				break;
			}
		}
	}else if (s=='U') {
		int nx = sx + dx[3];
		int ny = sy + dy[3];
		dir = 3;
		arr[sx][sy] = '^';
		char cur = arr[nx][ny];
		if (is_range(nx, ny)&&cur=='.') {//범위 밖을 벗어나지 않고
			arr[sx][sy] = '.';
			arr[nx][ny] = '^';
			sx = nx;
			 sy = ny;
		}
	}
	else if (s=='D') {
		int nx = sx + dx[2];
		int ny = sy + dy[2];
		dir = 2;
		arr[sx][sy] = 'v';
		char cur = arr[nx][ny];
		if (is_range(nx, ny) && cur == '.') {//범위 밖을 벗어나지 않고
			arr[sx][sy] = '.';
			arr[nx][ny] = 'v';
			sx = nx;
			sy = ny;
		}
	}
	else if (s == 'L') {
		int nx = sx + dx[1];
		int ny = sy + dy[1];
		dir = 1;
		arr[sx][sy] = '<';
		char cur = arr[nx][ny];
		if (is_range(nx, ny) && cur == '.') {//범위 밖을 벗어나지 않고
			arr[sx][sy] = '.';
			arr[nx][ny] = '<';
			 sx = nx;
			 sy = ny;
		}
	}
	else if (s == 'R') {
		int nx = sx + dx[0];
		int ny = sy + dy[0];
		dir = 0;
		arr[sx][sy] = '>';
		char cur = arr[nx][ny];
		if (is_range(nx, ny) && cur == '.') {//범위 밖을 벗어나지 않고
			arr[sx][sy] = '.';
			arr[nx][ny] = '>';
			 sx = nx;
			 sy = ny;
		}
	}
}


int main(){
	int T;

	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) {

			string tmp;
			cin >> tmp;
			for (int j = 0; j < tmp.size(); j++) {
				arr[i][j] = tmp[j];
				//오,왼,아래,위
				if (arr[i][j] == '<') {
					sx = i;
					sy = j;
					dir = 1;
				}
				else if (arr[i][j] == '>') {
					sx = i;
					sy = j;
					dir = 0;
				}
				else if (arr[i][j] == 'v') {
					sx = i;
					sy = j;
					dir = 2;
				}

				else if (arr[i][j] == '^') {
					sx = i;
					sy = j;
					dir = 3;
				}
			}
		}
		int I;
		cin >> I;
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); i++) {
			char c;
			c = s[i];
			func(c);
		}
		cout << "#" << t << " ";
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << arr[i][j];
			}
			cout << "\n";
		}
	}	
}