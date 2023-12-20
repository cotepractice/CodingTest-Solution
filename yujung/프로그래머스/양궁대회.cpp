#include <string>
#include <vector>

using namespace std;
vector<int> answer(1,-1);
int m = 0;

bool cmp(vector<int> a) {
    
    for(int i = 10; i >= 0; i--) {
        if(a[i] > answer[i]) return true;
        else if (a[i] < answer[i]) return false;
    }
}

void calc(vector<int> a, vector<int> b) {
    int ascore = 0;
    int bscore = 0;
    
    for(int i = 0; i < 11; i++) {
        if(a[i] > b[i]) ascore += 10 - i;
        else if(b[i] > 0) bscore += 10 - i;
    }
    
    int diff = ascore - bscore;
    if(diff > 0 && m <= diff) {
        if(m == diff && !cmp(a)) return;
        m = diff;
        answer = a;
    }
}


void dfs(int idx, int arrows, vector<int> a, vector<int> b) {
    if(idx==11 || arrows == 0) { //분배 끝 
        a[10] += arrows;
        calc(a,b);
        a[10] -= arrows;
        return;
    }
    if(b[idx] < arrows) {
        a[idx] += b[idx] +1;
        dfs(idx+1, arrows-b[idx]-1, a,b);
        a[idx] -= b[idx] +1;
    }
    dfs(idx+1, arrows, a, b);
}

vector<int> solution(int n, vector<int> info) {
    vector<int> a;
    
    dfs(0,n, a, info);

    if(answer.empty()) answer.push_back(-1);
    
    return answer;
}
