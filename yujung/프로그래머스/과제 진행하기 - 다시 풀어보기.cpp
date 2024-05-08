#include <string>
#include <vector>
#include<algorithm>
using namespace std;

bool cmp(vector<string>a,vector<string>b){
    return a[1]<b[1];
 }
vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    vector<pair<string,int>> wait;
    sort(plans.begin(),plans.end(),cmp);
    int time=0;
    for(int i=0; i<plans.size();i++){
        
        int new_time=60*stoi(plans[i][1].substr(0,2))+stoi(plans[i][1].substr(3,5));
        while(time<new_time){
            if(wait.size()>0){
                wait.back().second--;
                if(wait.back().second==0){
                    answer.push_back(wait.back().first);
                    wait.pop_back();
                }
            }
            time++;
        }
        wait.push_back({plans[i][0],stoi(plans[i][2])});
    }
    
    while(wait.size()>0){
        answer.push_back(wait.back().first);
        wait.pop_back();
    }
    
    return answer;
}