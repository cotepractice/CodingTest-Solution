#include <string>
#include <vector>
#include<map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string,int> m;
    for(auto a: clothes){
        m[a[1]]++;
    }
    for(auto i: m){
        answer*=(++i.second);
    }
    return answer-1;
}