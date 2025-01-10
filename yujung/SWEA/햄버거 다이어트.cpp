#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n, l;  // n: 재료 수, l: 칼로리 제한
vector<pair<int, int>> v; // {맛 점수, 칼로리} 저장
int ans = 0; // 최적의 맛 점수 저장

// DFS 탐색 함수
void dfs(int idx, int sum, int point) {
	// 종료 조건: 칼로리 합이 제한을 초과하면 종료
	if (sum > l) {
		return;
	}

	// 현재 점수 업데이트
	ans = max(ans, point);

	// 재료를 하나씩 선택하여 탐색
	for (int i = idx; i < n; i++) {
		dfs(i + 1, sum + v[i].second, point + v[i].first);
	}
}

int main() {
	cin >> n >> l; // 재료 수와 칼로리 제한 입력

	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b; // 맛 점수와 칼로리 입력
		v.push_back({ a, b });
	}

	// DFS 탐색 시작
	dfs(0, 0, 0);

	// 최적의 맛 점수 출력
	cout << ans;

	return 0;
}
