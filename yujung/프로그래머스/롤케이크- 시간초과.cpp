#include <string>
#include <vector>
#include<set>
#include<map>
using namespace std;
//1,000,000를 이중 반복문 돌리면 시간초과, 이를 hash map을 통해서 1차 반복문을 통해 해결
map<int,int> cnt;

int solution(vector<int> topping) {
    int answer = 0;
    int n=topping.size();
    set<int> s;
    
    if(topping.size()==1)return 0;
    bool f=true;
    for(int i=0;i<n;i++){
        s.insert(topping[i]);
        set<int>s1;
        for(int j=i+1;j<n;j++){
            s1.insert(topping[j]);
            if(s.size()<s1.size()){f=false;break;}
        }
        if(s.size()==s1.size()){
            answer++;
        }
    }
    return answer;
}