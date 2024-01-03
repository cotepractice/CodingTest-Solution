#include<iostream>
using namespace std;
#define MAX_N 51
#define MAX_P 31
int n, m, p, c, d;
int points[MAX_P];
pair<int, int> pos[MAX_P];
pair<int, int> rudolf;
int board[MAX_N][MAX_P];
bool is_live[MAX_P];
int stun[MAX_P];

const int dx[4] = { -1,0,1,0 };
const int dy[4] = { 0,1,0,-1 };

bool is_range(int x, int y) {
	return 1 <= x && x <= n && 1 <= y && y <= n;
}

void crash_rudolf_to_santa(int t, int closestIdx, int closestX, int closestY, int dirX, int dirY) {
	int firstX = closestX + dirX * c;
	int firstY = closestY + dirY * c;
	int lastX = firstX;
	int lastY = firstY;
	stun[closestIdx] = t + 1;
	while (is_range(lastX, lastY) and board[lastX][lastY] > 0) {
		lastX += dirX;
		lastY += dirY;
	}
	while (!(lastX == firstX and lastY == firstY)) {
		int beforeX = lastX - dirX;
		int beforeY = lastY - dirY;
		if (!is_range(beforeX, beforeY))break;

		int idx = board[beforeX][beforeY];

		if (!is_range(lastX, lastY)) {
			is_live[idx] = false;
		}
		else {
			board[lastX][lastY] = board[beforeX][beforeY];
			pos[idx] = { lastX,lastY };
		}
		lastX = beforeX;
		lastY = beforeY;
	}
	points[closestIdx] += c;
	pos[closestIdx] = { firstX,firstY };
	if (is_range(firstX, firstY)) {
		board[firstX][firstY] = closestIdx;
	}
	else {
		is_live[closestIdx] = false;
	}

}

//루돌프 움직이기
void rudolf_move(int t) {
	int closestX = 10000, closestY = 10000, closestIdx = 0;
	//살아있는 산타 중 루돌프에 가장 가까운 산타를 찾습니다.
	for (int i = 1; i <= p; i++) {
		if (!is_live[i])continue;
		pair<int, pair<int, int>> currentBest = { (closestX - rudolf.first)*(closestX - rudolf.first) + (closestY - rudolf.second)*(closestY - rudolf.second),{-closestX,-closestY} };
		pair<int, pair<int, int>> currentValue = { (pos[i].first - rudolf.first)*(pos[i].first - rudolf.first) + (pos[i].second - rudolf.second)*(pos[i].second - rudolf.second),{-pos[i].first,-pos[i].second } };

		if (currentValue < currentBest) {
			closestX = pos[i].first;
			closestY = pos[i].second;
			closestIdx = i;
		}
	}
	if (closestIdx) {
		pair<int, int> prevRudolf = rudolf;
		int moveX = 0;
		if (closestX > rudolf.first)moveX = 1;
		else if (closestX < rudolf.first)moveX = -1;
		int moveY = 0;
		if (closestY > rudolf.second)moveY = 1;
		else if (closestY < rudolf.second)moveY = -1;

		rudolf.first += moveX;
		rudolf.second += moveY;
		board[prevRudolf.first][prevRudolf.second] = 0;

		if (rudolf.first == closestX && rudolf.second == closestY) {
			crash_rudolf_to_santa(t,  closestIdx,  closestX, closestY,  moveX, moveY);
		}
		board[rudolf.first][rudolf.second] = -1;
	}
}



void crash_santa_to_rudolf(int t, int pid, int moveDir) {
	stun[pid] = t + 1;
	int nx = rudolf.first;
	int ny = rudolf.second;

	int moveX = -dx[moveDir];
	int moveY = -dy[moveDir];

	int firstX = nx + moveX * d;
	int firstY = ny + moveY * d;

	int lastX = firstX;
	int lastY = firstY;

	if (d == 1) {
		points[pid] += d;
	}
	else {
		while (is_range(lastX, lastY) and board[lastX][lastY] > 0) {
			lastX += moveX;
			lastY += moveY;
		}

		// 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
							// 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
		while (!(lastX == firstX and lastY == firstY)) {
			int beforeX = lastX - moveX;
			int beforeY = lastY - moveY;

			if (!is_range(beforeX, beforeY)) break;

			int idx = board[beforeX][beforeY];

			if (!is_range(lastX, lastY)) {
				is_live[idx] = false;
			}
			else {
				board[lastX][lastY] = board[beforeX][beforeY];
				pos[idx] = { lastX, lastY };
			}

			lastX = beforeX;
			lastY = beforeY;
		}
		points[pid] += d;
		board[pos[pid].first][pos[pid].second] = 0;
		pos[pid] = { firstX, firstY };
		if (is_range(firstX, firstY)) {
			board[firstX][firstY] = pid;
		}
		else {
			is_live[pid] = false;
		}
	}
}

void santa_move(int t) {
	for (int i = 1; i <= p; i++) {
		if (!is_live[i] || stun[i] >= t)continue;
		int minDist = (pos[i].first - rudolf.first)*(pos[i].first - rudolf.first) + (pos[i].second - rudolf.second)*(pos[i].second - rudolf.second);
		int moveDir = -1;
		for (int dir = 0; dir < 4; dir++) {
			int nx = pos[i].first + dx[dir];
			int ny = pos[i].second + dy[dir];
			if (!is_range(nx, ny) || board[nx][ny] > 0) continue;
			int dist = (nx - rudolf.first) * (nx - rudolf.first) + (ny - rudolf.second) * (ny - rudolf.second);
			if (dist < minDist) {
				minDist = dist;
				moveDir = dir;
			}
		}
		if (moveDir != -1) {
			int nx = pos[i].first + dx[moveDir];
			int ny = pos[i].second + dy[moveDir];
			if (nx == rudolf.first&&ny == rudolf.second) {
				crash_santa_to_rudolf(t, i, moveDir);
			}
			else {
				board[pos[i].first][pos[i].second] = 0;
				pos[i] = { nx, ny };
				board[nx][ny] = i;
			}
		}
		
	}
}




int main() {
	cin >> n >> m >> p >> c >> d;
	cin >> rudolf.first >> rudolf.second;
	board[rudolf.first][rudolf.second] = -1;
	for (int i = 1; i <= p; i++) {
		int id;
		cin >> id;
		cin >> pos[id].first >> pos[id].second;
		board[pos[id].first][pos[id].second] = id;
		is_live[id] = true;
	}
	for (int t = 1; t <= m; t++) {
		rudolf_move(t);
		santa_move(t);
		for (int i = 1; i <= p; i++)
			if (is_live[i]) points[i]++;
	}

	for (int i = 1; i <= p; i++)
		cout << points[i] << " ";
}