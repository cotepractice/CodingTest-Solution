#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<pair<int, int> >v[10001];
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > >pq;
bool visited[10001];
int sum;

void prim(int a)            // 프림 알고리즘 
{
	visited[a] = true;           // 시작 노드 방문  처리
	for (int i = 0; i < v[a].size(); i++)       // Node a와 연결된 방문 안한 다른 노드들 우선순위 큐에 넣기
	{
		if (!visited[v[a][i].second])
		{
			pq.push(make_pair(v[a][i].first, v[a][i].second));
		}
	}
	while (!pq.empty())
	{
		pair<int, int> pp = pq.top();
		pq.pop();
		if (!visited[pp.second])        // 방문하지 않은 노드 중 가장 가중치가 적은거 발견 시 그 노드를 인자값으로 prim함수 호출 후 함수 끝내기
		{
			sum += pp.first;
			prim(pp.second);
			return;
		}
	}
}
int main()
{
	int a, b;
	cin >> a >> b;
	for (int i = 1; i <= b; i++)        // 정점 연결과 가중지 입력.
	{
		int a1, a2, a3;                 // 정점 1, 정점 2, 가중치
		cin >> a1 >> a2 >> a3;
		v[a1].push_back(make_pair(a3, a2));
		v[a2].push_back(make_pair(a3, a1));
	}
	prim(1);                            // 첫번째 노드를 인자값에 넣어 prim 함수 호출
	cout << sum;
	return 0;
}
