#include <string>
#include <vector>
#include<stack>
using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> s;
    int oi=0;//order순서
    int idx=1;
    int tmp=order[0];
    while(oi<order.size()){
       // i++;
        if(idx<order[oi]){   //4<5
               s.push(idx); //1,2,3
        
            idx++;
        }
        if(idx==order[oi]){ //4==order[4]
            oi++; //1 
            idx++; //5
            answer++; //
        }
        
       
        if(idx>order[oi]){ //5>4
           if(s.top()==order[oi]){ //3== order[1]
              answer++;
               oi++;
               s.pop();
           }else{break;}
        }
    }
        
        
    return answer;
}