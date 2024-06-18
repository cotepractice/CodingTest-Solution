#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
 
// 1 1 0 0 1 1 0인 경우 최소 4인데 5로 잘못 출력됨 
int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		vector<string> v;
		
		queue<string> q1;
		queue<string>q2;
		string s;

		int tmp = 0;
		if (n % 2 == 1) {
			tmp += n / 2 + 1;
		}
		else {
			tmp = n / 2;
		}
		for (int i = 0; i < tmp; i++) {
	
			cin >> s;//s를 넣어
			
			q1.push( s );
		}
		for (int i = tmp; i < n; i++) {
		
			cin >> s;//s를 넣어

			q2.push(s);
		}
		for (int i = 0; i < n/2; i++) {
			string a = q1.front();
			string b = q2.front();
			q1.pop();
			q2.pop();
			v.push_back(a);
			v.push_back(b);
		}
		
		
		if (n % 2 == 1) {
			
			v.push_back(q1.front());
		}
		cout << "#"<<t<<" ";
		for (int i = 0; i < n; i++) {
			cout << v[i] << " ";
		}
		cout<<"\n";
	}

	
}