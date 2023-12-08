#include <string>
#include <vector>
#include<queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int,vector<int>, greater<int>> pq;
    int answer = 0;
    for(auto a: scoville){
        pq.push(a);
    }
    int sum=0;
    while(pq.size()>=2&&pq.top()<K){
        sum=0;
        int first=pq.top();
        pq.pop();
        int second=pq.top();
        pq.pop();
        sum=first+second*2;
        pq.push(sum);
        answer++;
    }
   if(!pq.empty()&&pq.top()<K) return -1;
    return answer;
}