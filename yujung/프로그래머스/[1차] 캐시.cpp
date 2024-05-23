#include <string>
#include <vector>
#include<deque>
#include<algorithm>
using namespace std;


int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    deque<string> dq;
    
    for(int i=0; i<cities.size();i++){
        if(cacheSize==0)break;
        string tmp;
        for(int j=0; j<cities[i].size();j++){
            tmp+=to_string(tolower(cities[i][j]));
        }
        auto it=find(dq.begin(),dq.end(),tmp);
        if(it==dq.end()){ //찾지 못했으면 넣어야 함
             if(dq.size()<cacheSize){ //캐시사이즈가 작으면 넣으면 됨
            dq.push_front(tmp);
        }else{
                 dq.pop_back();
                 dq.push_front(tmp);
             }
            answer+=5;
        }else{//찾았다면
          
                 dq.erase(it);
                 dq.push_front(tmp);
                 
             answer++;
        }
       
    }
    if(cacheSize==0){
        answer=1;
        answer*=cities.size()*5;
    }
    
    return answer;
}