#include<iostream>
#include<queue>
using namespace std;

int N;
queue<pair<int, int>> q;
int res = 0;
pair<int, int> s;
pair<int, int> e;

struct c {
	int x, y;
	bool visited;
};
vector<c> convi;





string bfs(int x, int y)
{
	q.push({ x,y });

	while (!q.empty())
	{
		int cx = q.front().first;
		int cy = q.front().second;
		q.pop();
		for (int i = 0; i < convi.size(); i++)
		{
			int ax = convi[i].x;
			int ay = convi[i].y;
			if (convi[i].visited == true)continue;
			if (abs(cx - ax) + abs(cy - ay) <= 1000) {
				q.push({ ax,ay });
				convi[i].visited = true;
			}
		}
		if (abs(cx - e.first) + abs(cy - e.second) <= 1000) { 
			while (!q.empty()) {
				q.pop();
			}
			return "happy"; }
	}
	return "sad";
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		convi.clear();
		cin >> N;
		int a, b;
		cin >> a >> b;
		s = { a,b };
		//상근이 집
		for (int i = 1; i <= N; i++)
		{
		
			cin >> a >>b ;
			c h = { a  ,b ,false };
			convi.push_back(h);
		}
		cin >> a >> b;
		e = { a ,b };

		cout << bfs(s.first, s.second)<<"\n";
	}
	

}