#include <string>
#include <vector>
#include<algorithm>
using namespace std;
 int answer ;
void func(int cnt,string s){
    for(int i=0; i<s.size();){
        string cmp= s.substr(i,cnt);
        int same=1;
        for(int j=i+cnt;j<s.size();j+=cnt){
            if(cmp==s.substr(j,cnt)){
                same++;
            }else{
                break;
            }
        }
        if(same==1){
            i+=cnt;
            continue;
        }
        string a=s.substr(0,i);
        string b=to_string(same)+cmp;
        string c=s.substr(i+same*cnt);
        s=a+b+c;
        i+=b.size();
     
      
    }
     int ss=s.size();
      answer=min(answer,ss);
}
int solution(string s) {
    answer =s.size();// 압축을 못한다면 원래크기, 중요: 안할 경우 틀림
    int n=s.size()/2;
    for(int i=1;i<=n;i++){
        func(i, s);
    }
    return answer;
}