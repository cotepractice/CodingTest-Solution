#include<iostream>
using namespace std;

const int MAX_N = 2187; // NxN의 최대 크기는 3^7 = 2187

int arr[MAX_N][MAX_N];
int cnt = 0;
int ans[3] = { 0,0,0 };
int tmp = 2;
// 주어진 부분 행렬이 모두 같은 숫자로 이루어져 있는지 확인하는 함수
bool check(int x, int y, int n) {
    int target = arr[x][y];
    for (int i = x; i < x + n; i++) {
        for (int j = y; j < y + n; j++) {
            if (arr[i][j] != target) {
                return false;
            }
        }
    }
    tmp = target;
    return true;
}

// 주어진 행렬을 나누고, 재귀적으로 호출하여 카운트를 증가시키는 함수
void recur(int x, int y, int n) {
    // 주어진 부분 행렬이 모두 같은 숫자로 이루어져 있으면 카운트 증가
    if (check(x, y, n)) {
        if (tmp == -1) {
            ans[0]++;
        }
        else if (tmp == 0) {
            ans[1]++;
        }
        else if (tmp == 1) {
            ans[2]++;
        }
        tmp = 2;
        return;
    }

    // 주어진 행렬을 9개의 부분 행렬로 나누어서 재귀 호출
    int m = n / 3; // 3으로 나눈 부분 행렬의 크기
    for (int i = 0; i < n; i+=m) {
        for (int j = 0; j < n; j+=m) {
            recur(i+x , j+y,  m); // 부분 행렬의 시작 위치와 크기를 재귀 호출
        }
    }
   

}

int main() {
    int n;
    cin >> n;

    // 행렬 입력 받기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    // 재귀 호출 시작
    recur(0, 0, n);

    // 결과 출력
    for (int i = 0; i < 3; i++) {
        cout << ans[i] << endl;
    }
   

    return 0;
}
