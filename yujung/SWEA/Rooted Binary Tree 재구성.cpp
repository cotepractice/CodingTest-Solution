#include<iostream>
#include<queue>
using namespace std;

int arr[1024];
int visited[1024];
vector<int>tmp;
void check() {
	int sum = 1;
	tmp.push_back(sum);
	int n = 1;
	
	for (int i = 0; i < 9; i++) {
		n *= 2;
		sum += n;
		tmp.push_back(sum);
	}
}
void bfs(int start, int end,int t) {
	cout << "#" << t << " ";
	queue<pair<int,int>> q;
	q.push({ start,end });
	int cnt = 0;
	int idx = 0;
	while (!q.empty()) {
		cnt++;
		pair<int,int> a=q.front();
		q.pop();
		int mean = (a.first + a.second)/2;
		
		if (a.first != a.second) {
			cout << arr[mean] << " ";
			
			if (cnt == tmp[idx]) {
				cout << "\n";
				idx++;
			}
			
			q.push({ a.first,mean });
			q.push({ mean + 1,a.second });
		}
	}

}
int main() {
	int T;
	check();
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		int num = 1;
		for (int i = 0; i < n; i++) {
			num *= 2;
		}
		num--;
		for (int i = 0; i < num; i++) {
			cin >> arr[i];
		}
		
		bfs(0, num,t);
	}
	
	/*int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		
		cout << '#' << t<< ' ' << score << '\n';
	}
	return 0;*/
}