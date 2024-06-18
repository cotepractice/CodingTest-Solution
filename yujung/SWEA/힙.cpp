#include<iostream>
#include<queue>
#include<vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		vector<int> v;
		priority_queue<int, vector<int>> q;
		for (int i = 0; i < n; i++) {
			int a;
			cin >> a;
			if (a == 1) {
				int b;
				cin >> b;
				q.push(b);
			}
			else if (a == 2) {
				if (q.empty()) {
					v.push_back(-1);
				}
				else {
					v.push_back(q.top());
					q.pop();
				}
			}
		}
		cout << "#" <<t<< " ";
		for (int i = 0; i < v.size(); i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
	}
	
	

}