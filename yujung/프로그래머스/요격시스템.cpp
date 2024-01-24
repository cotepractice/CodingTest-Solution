#include <string>
#include <vector>
#include<algorithm>

using namespace std;

int solution(vector<vector<int>> targets) {
    int answer = 0;
    sort(targets.begin(), targets.end(), [&](vector<int> &v1, vector<int> &v2) {
		return v1[1] < v2[1];
	});
    
    int firstB=-1;
    for(int i=0;i<targets.size();i++){
        if(firstB<=targets[i][0]){
            answer++;
            firstB=targets[i][1];
        }
    }
    return answer;
}