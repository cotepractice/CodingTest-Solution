#include<iostream>
#include<vector>
using namespace std;
int n;
vector<pair<int, int>> v;

void hanoi(vector<pair<int,int>>& answer,int n, int start, int dest) {
	if (n == 1)
	{
		answer.push_back({ start,dest });
		return;
	}
	hanoi(answer, n - 1, start, 6 - start - dest);
	answer.push_back({ start, dest });
	hanoi(answer, n - 1, 6 - start - dest, dest);
}

int main() {
	cin >> n;
	hanoi(v, n, 1, 3);

	cout << v.size()<<endl;
	for (int i = 0; i < v.size(); i++) {
		cout << v[i].first <<" "<< v[i].second<<endl;
	}

}