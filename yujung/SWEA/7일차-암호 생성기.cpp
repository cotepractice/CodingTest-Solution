#include<iostream>
#include<queue>
using namespace std;


int main() {
	
	for (int t = 1; t <= 10; t++) {
		int T;
		cin >> T;
		queue<int> q;
		for (int i = 0; i < 8; i++) {
			int a;
			cin >> a;
			q.push(a);
		}
		bool f = false;
		while (1) {
			for (int i = 1; i <= 5; i++) {
				int num = q.front();
				q.pop();
				num -= i;
				if (num <= 0) {
					num = 0;
				}
				q.push(num);
				if (num <= 0) {
					f = true;
					break;
				}
			}
			if (f == true) { break; }
		}

		
		cout << "#" << t << " ";
		while (!q.empty()) {
			int a = q.front();
			cout << a << " ";
			q.pop();
		}
		cout<< "\n";
	}
	
}