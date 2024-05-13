#include <string>
#include <vector>
#include<map>
using namespace std;

map<int,int> m;
int solution(vector<int> topping) {
    
    int answer = 0;
     for(int i=0; i<topping.size();i++){
         m[topping[i]]++;
     }
       map<int,int> brother;
    for(int i=0; i<topping.size();i++){
        if(brother.size()>m.size())break; //효율 높이기
        if(m.find(topping[i])!=m.end()){
            m[topping[i]]--;
            brother[topping[i]]++;
        }
        if(m[topping[i]]==0){
            m.erase(topping[i]);
        }
        if(brother.size()==m.size()){
            answer++;
        }
    }
    return answer;
}