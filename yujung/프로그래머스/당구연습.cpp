#include <string>
#include <vector>
#include <cmath>
//공이 목표 공에 맞기 전에 멈추는 경우는 없으며, 목표 공에 맞으면 바로 멈춤

using namespace std;

int calc_dist(int m, int n, int a, int b, int c, int d) {
    int minDist = 987654321;
    // 아래 벽 기준 반전. 같은 x좌표의 경우 예외.
    if (a != c || b <= d) 
        minDist = min(minDist, (int)(pow(a - c, 2) + pow(b + d, 2)));
    // 오른쪽 벽 기준 반전. 같은 y좌표의 경우 예외.
    if (a >= c || b != d) 
        minDist = min(minDist, (int)(pow(a - 2 * m + c, 2) + pow(b - d, 2)));
    // 위쪽 벽 기준 반전. 같은 x좌표의 경우 예외.
    if (a != c || b >= d) 
        minDist = min(minDist, (int)(pow(a - c, 2) + pow(b - 2 * n + d, 2)));
    // 왼쪽 벽 기준 반전. 같은 y좌표의 경우 예외.
    if (a <= c || b != d) 
        minDist = min(minDist, (int)(pow(a + c, 2) + pow(b - d, 2)));
    return minDist;
}

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;
    for (int i = 0; i < balls.size(); i++) {
        answer.push_back(calc_dist(m, n, startX, startY, balls[i][0], balls[i][1]));
    }
    return answer;
}