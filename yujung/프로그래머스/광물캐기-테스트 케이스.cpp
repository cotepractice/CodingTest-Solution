#include <string>
#include <vector>
#include<map>
using namespace std;
map<string, int> m;
int score[3][3] = { {1,1,1},{5,1,1},{25,5,1} };
void dfs(vector<int> & picks, vector<string>  minerals,int &answer,int sum,int location) {
	if (location == minerals.size() || (picks[0] == 0 && picks[1] == 0 && picks[2] == 0)) {
		answer=min(answer,sum);
		return;
	}
	for (int i = 0; i < 3; i++) {
		if (picks[i] != 0) {
			picks[i]--;
			int tot=sum;
            int j = location;
			for (; j < location + 5&&j<minerals.size(); j++) {
				tot+=score[i][m[minerals[j]]];
			}

			dfs(picks, minerals, answer,tot, j);
            picks[i]++;
		}
        
	}
}
int solution(vector<int> picks, vector<string> minerals) {
	int answer = 25*50+1;
	m.insert({"diamond", 0});
	m.insert({ "iron", 1 });
	m.insert({ "stone", 2 });
	dfs(picks, minerals, answer, 0, 0);
	return answer;
}