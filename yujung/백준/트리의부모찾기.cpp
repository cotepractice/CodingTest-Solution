#include<iostream>
#include<vector>
# define MAX 100001
using namespace std;

int n;
bool visited[MAX];
int parent[MAX];
vector <int> tree[MAX];

void findParent(int nodeNum) {
	visited[nodeNum] = true;
	for (int i = 0; i < tree[nodeNum].size(); i++)
	{
		int next = tree[nodeNum][i];
		if (!visited[next])
		{
			parent[next] = nodeNum;
			findParent(next);
		}
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int node1, node2;
		cin >> node1 >> node2;
		tree[node1].push_back(node2);
		tree[node2].push_back(node1);
	}
	findParent(1);

	for (int i = 2; i <= n; i++) {
		cout << parent[i] << "\n";
	}
}