#include <string>
#include <vector>
#include<map>
using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string, int> m;
    map<string,int> tmp;
    for(int i=0; i<want.size();i++){
        m[want[i]]=number[i];
        tmp[want[i]]=number[i];
    }
    bool f=false;
    for(int i=0; i<discount.size()-9;i++){
        m=tmp;
        f=false;
        for(int j=i;j<i+10;j++){
                 m[discount[j]]--;   
        }
        for(auto w: want){
            if(m[w]>0){
                f=true;
                break;
            }
        } 
        if(!f){
               answer++;
        }
     
    }

    
    return answer;
}