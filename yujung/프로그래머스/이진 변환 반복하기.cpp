#include <string>
#include <vector>

using namespace std;

int remove_0=0;
int res=0;
string func(int n){
    string s1;
    while(n>0){
        string a= to_string(n%2);
        s1+=a;
        n/=2;
    }
    return s1;
}

void play(string s,int cnt){
      int a=0;
    int b=0;
    for(int i=0; i<s.size();i++){
        if(s[i]=='0') a++;
        else if(s[i]=='1')b++;
    }

    string tmp=func(b);
        remove_0+=a;
    if(tmp=="1"){
        res=cnt;
        return ;
    }
    
    
   
    play(tmp,cnt+1);
    
}
vector<int> solution(string s) {
    vector<int> answer;
  play(s,1);
    answer.push_back(res);
    answer.push_back(remove_0);
    
    
    return answer;
}