#include <string>
#include <vector>
#include<queue>
#include<algorithm>
using namespace std;

struct cmp{//우선순위큐에서 우선순위를 재정의하는 compare 구조체, sort와 반대임
    bool operator()(vector<int> a, vector<int> b){
        return a[1]>b[1];
    }
};
int solution(vector<vector<int>> jobs) {
    int total_time = 0;
    int current_time=0;
    int idx=0;
    sort(jobs.begin(),jobs.end()); //jobs.size()--> 도착 순서
    priority_queue<vector<int>, vector<vector<int>>, cmp> pq; //우선순위 큐
        
    while(idx<jobs.size()||!pq.empty()){ //!pq.empty()을 하는 이유는  아래 if문에서 continue를 하니까 pq가 남아 있을 수 도 있음
        if(idx<jobs.size()&&current_time>=jobs[idx][0]){
            pq.push(jobs[idx]); //현재 시간보다 먼저 도착해 있는 애들끼리 비교해서 실행 시간이 짧은 순서대로 정렬
            idx++;
            continue;
        }
        
        if(!pq.empty()){ //미리 도착해 있는 경우
            current_time+=pq.top()[1]; //현재 시간
            total_time+=current_time-pq.top()[0]; //기다린 시간
            pq.pop();
            
        }else{ //도착해있지 않은 경우
            current_time=jobs[idx][0];
        }
    }
    return total_time/jobs.size();
}