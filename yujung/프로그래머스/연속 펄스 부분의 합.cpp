#include <string>
#include <vector>

using namespace std;


long long solution(vector<int> sequence) {
    long long answer = 0;
    long long dp[500001];
    
    for(int i=0; i<sequence.size();i++){
        if(i%2==0){
            sequence[i]*=-1;
        }
    }
  
    dp[0]=sequence[0];
 
    for(int i=1; i<sequence.size();i++){
       dp[i]=max((long long)sequence[i]+dp[i-1],(long long)sequence[i]);
    }
    long long max_v=-1;
     for(int i=0; i<sequence.size();i++){
       if(max_v<dp[i]){
           max_v=dp[i];
       }
    }
    
    
    for(int i=0; i<sequence.size();i++){
        if(i%2==0){
            sequence[i]*=-1;
        }else{
            sequence[i]*=-1;
        }
    }
  
        dp[0]=sequence[0];
    
    for(int i=1; i<sequence.size();i++){
       dp[i]=max((long long)sequence[i]+dp[i-1],(long long)sequence[i]);
    }
 
     for(int i=0; i<sequence.size();i++){
       if(max_v<dp[i]){
           max_v=dp[i];
       }
    }
    
    return max_v;
}