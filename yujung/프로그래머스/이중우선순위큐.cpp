#include <string>
#include <vector>
#include<deque>
#include<algorithm>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    deque<int> dq;
    for(int i=0; i<operations.size();i++){
        int a=operations[i][0];
        int c=stoi(operations[i].substr(2));
        if(a=='I'){
            dq.push_back(c);
        }else{
            if(dq.empty())continue;
            sort(dq.begin(),dq.end());
            if(c==1){
                dq.pop_back();
            }else{ 
                dq.pop_front();
            }
        }
    }
    if(dq.empty()){
        return {0,0};
    }else{
        sort(dq.begin(),dq.end());
        return {dq.back(),dq.front()};
    }

}