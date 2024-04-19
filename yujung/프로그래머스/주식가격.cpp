#include <string>
#include <vector>
//price [1,2,3,2,3] []
using namespace std;
//가격이 떨어지지 않은 기간
vector<int> solution(vector<int> prices) {
    vector<int> answer;
   
    for(int i=0; i<prices.size()-1;i++){
        int cnt=0;
      for(int j=i+1; j<prices.size();j++){
        
              cnt++; //하락 한번해도 초 개수 세기 위해 if문 앞에 작성
      
           if(prices[i]>prices[j]){
              break;
          }
         
      }
        answer.push_back(cnt);
        
    }
 
    answer.push_back(0);
    return answer;
}

