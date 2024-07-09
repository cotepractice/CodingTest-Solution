#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<vector<string>> v;
int make_second(int h, int m) {
    return h * 60 + m;
}

bool cmp(vector<string> a, vector<string> b) {
    return stoi(a[1]) < stoi(b[1]);
}

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    vector<pair<string, int>> wait;

    for(int i = 0; i < plans.size(); i++) {
        int h = stoi(plans[i][1].substr(0, 2));
        int m = stoi(plans[i][1].substr(3, 2));
        int total = make_second(h, m);
        plans[i][1] = to_string(total);
    }

    sort(plans.begin(), plans.end(), cmp);

    int time = 0;
    for(int i = 0; i < plans.size(); i++) {
        int new_time = stoi(plans[i][1]);
        
        while (time < new_time) {
            if (!wait.empty()) {
                wait.back().second--;
                if (wait.back().second == 0) {
                    answer.push_back(wait.back().first);
                    wait.pop_back();
                }
            }
            time++;
        }
        
        wait.push_back({plans[i][0], stoi(plans[i][2])});
    }
    
    while (!wait.empty()) {
        answer.push_back(wait.back().first);
        wait.pop_back();
    }
    
    return answer;
}