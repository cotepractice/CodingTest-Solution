//무조건 좋은 곡괭이부터 쓴다고 좋은 것이 아님

#include <string>
#include <vector>
#include<iostream>
using namespace std;
//광산에 있는 모든 광물을 캐거나, 더 사용할 고괭이가 없을 때까지
int solution(vector<int> picks, vector<string> minerals) {
    int answer = 0;

    int n = minerals.size();
    int m = minerals[0].size();
    int idx = 0;
    int flag = false;
    for (int i = 0; i < picks.size(); i++) {
        while (picks[i] > 0) {
            for (int j = 0; j < 5; j++) {
                if (idx >= n) { flag = true; break; }//광물을 다캤으면 그만
                if (i == 0) {
                    if (minerals[idx] == "diamond") {
                        answer += 1;
                    }
                    else if (minerals[idx] == "iron") {
                        answer += 1;
                    }
                    else if (minerals[idx] == "stone") {
                        answer += 1;
                    }
                }
                else if (i == 1) {
                    if (minerals[idx] == "diamond") {
                        answer += 5;
                    }
                    else if (minerals[idx] == "iron") {
                        answer += 1;
                    }
                    else if (minerals[idx] == "stone") {
                        answer += 1;
                    }

                }
                else if (i == 2) {
                    if (minerals[idx] == "diamond") {
                        answer += 25;
                    }
                    else if (minerals[idx] == "iron") {
                        answer += 5;
                    }
                    else if (minerals[idx] == "stone") {
                        answer += 1;
                    }

                }
                idx++;
            }
            
            picks[i]--;
            if (flag) { break; }
        }
        if (flag) { break; }
    }
    return answer;
}

int main() {
    vector<int> picks={ 1, 3, 2 };
    vector<string> minerals={ "diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone" };
    cout<<solution( picks, minerals);

}