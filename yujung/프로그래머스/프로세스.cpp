#include <string>
#include <vector>
#include<queue>
#include<algorithm>
using namespace std;


int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int,int>> q;
    for(int i=0; i<priorities.size();i++){ 
        q.push({priorities[i],i}); 
    }
    

    int idx=0;
    sort(priorities.begin(),priorities.end(),greater<int>());
    int cnt=0;
    while(!q.empty()){
        pair<int,int> a=q.front();
   
        if(a.first==priorities[idx]){
            cnt++;
            idx++;
            if(a.second==location){
                answer=cnt;
                break;
            }
                 q.pop();
            
        }else{
          q.pop();
          q.push(a);  
        }
    }
    return answer;
}