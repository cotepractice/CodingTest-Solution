#include<iostream>
#include<queue>
#include<vector>
using namespace std;
#define MAX_N 1001
int v, e;

int cnt[MAX_N];
int main()
{
	vector<int> vec[MAX_N];
	queue<int>q;
	cin >> v >> e;
	for (int i = 0; i < e; i++) {
		int a, b;
		cin >> a >> b;
		vec[a].push_back(b);
		cnt[b]++;
	}

	for (int i = 1; i <= v; i++)
	{
		if (cnt[i] == 0)
		{
			cout << i << " ";
			q.push(i);
		}
	}
	while (!q.empty()) {
		int vertex = q.front();
		q.pop();

		for (int i = 0; i < vec[vertex].size(); i++)
		{
			cnt[vec[vertex][i]]--;
			if (cnt[vec[vertex][i]] == 0)
			{
				cout << vec[vertex][i] << " ";
				q.push(vec[vertex][i]);
			}
		}
	}

}