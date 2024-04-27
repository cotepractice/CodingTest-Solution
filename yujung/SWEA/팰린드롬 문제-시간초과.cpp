#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int n, m;
int visited[100];
vector<string> v;
string arr[100];
int answer = 0;
bool check(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] != s[s.size() - i-1]) { return false; }
	}
	return true;
}
void dfs(int cnt,int l) {
	if (cnt == l) {
		string ans;
		for (int i = 0; i < v.size(); i++) {
			ans += v[i];
		}
		//cout << ans << "\n";
		if (check(ans)) { //앞과 뒤가 같음
		//	cout <<"중요"<< ans << "\n";
			int a = ans.length();
			answer=max(answer, a);
		};
		return;
	}
	for (int i = 0; i < n; i++) {
		if (visited[i] == true)continue;
		visited[i] = true;
		v.push_back(arr[i]);
		dfs(cnt + 1,l);
		v.pop_back();
		visited[i] = false;
	}
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			string a;
			cin >> a;
			arr[i] = a;
		}
		for (int i = n; i >= 1; i--) {
			dfs(0, i);
		}

		//cout<<"중요"<<check("racecar");
		cout <<"#"<<t<<" "<<answer<<"\n";
		answer = 0;
	}
	
}