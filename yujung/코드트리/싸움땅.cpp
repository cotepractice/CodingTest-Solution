#include<iostream>
#include<queue>
using namespace std;
#define MAX_N 21
#define MAX_M 31


priority_queue<int> board[MAX_N][MAX_N]; 

int n, m, k;

struct s {
	int x, y, d, s,gun;
};
vector<s> player;
int score[MAX_M];

int dx[4] = {-1,0,1,0};// ↑, →, ↓, ←
int dy[4] = {0,1,0,-1};

//첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다. 만약 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동합니다.
int is_people(int idx) {
	for (int i = 1; i <= m; i++) {
		if (i == idx)continue;
		if (player[idx].x == player[i].x&&player[idx].y == player[i].y) {//위치가 같다면
			return i;
		}
	}
	return 0;
}

bool is_range(int x, int y) {
	return x > 0 && y > 0 && x <= n && y <= n;
}
void win(int p) {
	int x = player[p].x;
	int y = player[p].y;
	int gun = player[p].gun;
	if(gun>0){ //총 가지고 있으면
		board[x][y].push(gun);
		player[p].gun = 0;
	}
	if (board[x][y].size() > 0) {
		player[p].gun=board[x][y].top();
		board[x][y].pop();
	}
}

void loser(int p) {
	int x=player[p].x;
	int y = player[p].y;
	int s = player[p].s;
	int d = player[p].d;
	int gun = player[p].gun;

	if (gun > 0) {
		board[x][y].push(gun); //총 버리고
		player[p].gun = 0;
	}
	int nx = x + dx[d];
	int ny = y + dy[d];
	player[p].x = nx;
	player[p].y = ny;
	while (is_people(p) || !is_range(nx,ny)) { //이동한자리에 다른 사람 있거나 범위 밖인 겨웅
		 //9도 회전
		d = (d + 1) % 4;
		nx = x + dx[d];
		ny = y + dy[d];
		player[p].x = nx;
		player[p].y = ny;
	}
	player[p].d = d;

	if (board[nx][ny].size() > 0) {//이동한 곳에 총 있으면 주움
		player[p].gun = board[nx][ny].top();
		board[nx][ny].pop();
	}
}

//1-1. 첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다. 만약 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동합니다.
void move() {
	for (int i = 1; i <= m; i++) {
		int x = player[i].x;
		int y = player[i].y;
		int d = player[i].d;
		int s = player[i].s;
		int gun = player[i].gun;

		int nx = x + dx[d];
		int ny = y + dy[d];
		if (nx<1 || ny<1 || nx>n || ny>n) {
			d=(d + 2) % 4;
			nx = x + dx[d];
			ny = y + dy[d];
		}

		player[i].x = nx;//실질적 이동
		player[i].y = ny;
		player[i].d = d; 
		x = nx;
		y = ny;
		//이동한 후에 
		int p = is_people(i);
		if (p==0) { //이동한 방향에 플레이어가 없는 경우
			//해당 칸에 총이 있는지 확인
			if (player[i].gun > 0) { //총을 가지고 잇는 경우
			
				board[x][y].push(player[i].gun); //떨구고
				player[i].gun = 0;
			}
			if (board[x][y].size() > 0) { //그 자리에 총이 있으면
				player[i].gun = board[x][y].top();//제일 큰 값 주움
				board[x][y].pop();
			}
		}
		else {//있는 경우
			int cs = player[p].s;
			int cgun = player[p].gun;
			if (s + gun > cs + cgun) {
				score[i] += (s + gun) - (cs + cgun);
				loser( p);
				win(i);
			}
			else if(s+gun<cs+cgun){
				score[p] +=  (cs + cgun)- (s + gun);
				loser(i);
				win(p);
			}
			else {
				if (s > cs) {
					loser(p);
					win(i);
				}
				else {
					loser(i);
					win(p);
				}

			}
		}

	}
}


int main() {
	cin >> n >> m >> k;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			int a;
			cin >> a;
			if (a > 0) { //총이 있으면 넣기
				board[i][j].push(a);
			}
		}
	}
	player.push_back({ 0,0,0,0 });
	for (int i = 1; i <= m; i++) {
		int x, y,d,s ;
		cin >> x >> y >> d >> s;
		player.push_back({ x,y,d,s,0 });
	}
	while (k--) {
		move();
	}
	for (int i = 1; i <= m; i++) {
		cout << score[i] << " ";
	}
}