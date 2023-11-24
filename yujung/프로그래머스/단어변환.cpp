//단어 변환

#include<iostream>
#include <string>
#include <vector>
#include<algorithm>

using namespace std;

bool visited[50] = { false, };
int answer=50;

bool check(string a, string b)
{
	int cnt = 0;
	int l = a.size();
	for (int i = 0; i < l; i++) {
		if (a[i] != b[i]) {
			cnt++;
		}
	}
	if (cnt == 1) {
		return true;
	}
	return false;
}
void dfs(string begin, string target, vector<string> words,int step) {

	if (answer <= step) {
		return;
	}
	
	if (begin == target) {
		answer = min(answer, step);
		return ;
	}
	for (int i = 0; i < words.size(); i++) {
		if (check(begin, words[i]) == true && visited[i] == false)
		{
			
			visited[i] = true;
		//	cout << begin << " " << visited[i];
			dfs(words[i], target, words,step+1);
			visited[i] = false;
			
		
		}
	}	

	return ;
}

int solution(string begin, string target, vector<string> words) {
	dfs(begin, target, words, 0);
	if (answer == 50)
		return 0;
	return answer;
}




int main() {

	string b;
	string t;
	vector<string> w;
	int n;
	string tmp;

	cin >> b;
	cin >> t;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		w.push_back(tmp);
	}
	cout<<solution(b,t, w);
	//cout << answer ;
}