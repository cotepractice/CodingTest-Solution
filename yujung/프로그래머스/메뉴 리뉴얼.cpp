#include <string>
#include <vector>
#include<map>
#include<algorithm>
using namespace std;

map<string,int> m;
void dfs(string order,string tmp,int len,int next){
    if(len==tmp.size()){
        m[tmp]++;
    }
    for(int i=next; i<order.size();i++){
        dfs(order,tmp+order[i],len,i+1);
    }
}
vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    for(int i=0; i<course.size();i++){
        for(int j=0; j<orders.size();j++){
            sort(orders[j].begin(),orders[j].end());
            dfs(orders[j], "",course[i],0);
        }
        int max_size=0;
        for(auto a: m){
            if(max_size<a.second){
                max_size=a.second;
            }
        }
        if(max_size<2)continue;
        else{
            for(auto a:m){
                if(max_size==a.second){
                    answer.push_back(a.first);
                }
            }
        }
        m.clear();
    }
    sort(answer.begin(),answer.end());
    return answer;
}