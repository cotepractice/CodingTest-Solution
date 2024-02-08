#include <string>
#include <vector>
#include<cmath>
#include<queue>
using namespace std;

queue<int> q;
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int cnt=1;
    int max=0;
    for(int i=0; i<progresses.size();i++){
    progresses[i]=100-progresses[i];
    progresses[i]=ceil((float)progresses[i]/speeds[i]);
        q.push(progresses[i]);
    }
    while(!q.empty()){
        max=q.front();
        q.pop();
        while(!q.empty()&&max>=q.front()){
            q.pop();
            cnt++;
        }
        answer.push_back(cnt);
        cnt=1;
    }
    
    return answer;
}