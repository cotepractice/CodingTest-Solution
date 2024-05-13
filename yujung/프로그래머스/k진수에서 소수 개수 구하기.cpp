//n k진수로 밖
#include <string>
#include <vector>
#include<algorithm>
#include<cmath>
using namespace std;
//소수 체크
bool is_prime(long long n){
    if(n==0||n==1)return false;
    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0)return false;
    }
    return true;
}

string trans(int n , int k){
    string s;
    while(n>0){
        s+=to_string(n%k);
        n/=k;
    }
    reverse(s.begin(),s.end());
    return s;
}

int solution(int n, int k) {
    
    string s=trans(n ,  k);

    
   int answer=0;
 
    bool f=false;
    for(int i=0; i<s.size();i++){
        string tmp;
          if(s[i]=='0'){
              f=false;
              tmp="";
              continue;
          }
        while(s[i]!='0'&&i<s.size()){
            tmp+=s[i];
             i++;
             if (i >= s.size() || s[i] == '0') { //마지막에 0이 아닌 숫자로 끝날 수 있으니까 check를 무조건 해줘야함
                f = true;
                break;
            }
           
        }
        if(f){
              if(is_prime(stol(tmp))){
                  answer++;
              }
        }
      
    }
    
    return answer;
}