#include <string>
#include <vector>
#include<stack>
using namespace std;

    int answer = 0;

void func(string s){
     stack<char> st;
    int idx=0;
    bool f=false;
    while(idx<s.size()){
        if(s[idx]=='[' ||s[idx]=='(' ||s[idx]=='{' ){
            f=true;
            st.push(s[idx]);
      
        }
        if(st.top()=='[' &&s[idx]==']'){
            st.pop();
        }
        if(st.top()=='(' &&s[idx]==')'){
            st.pop();
        }
        if(st.top()=='{'&&s[idx]=='}'){
            st.pop();
        }
            
        idx++;
    }
    if(st.empty()&&f){ //
       answer++;
    }
}


int solution(string s) {

    for(int i=0;i<s.size();i++){
         func(s);
        char tmp=s.front();
        s.erase(s.begin());
        s.push_back(tmp);
       
    }
 
    return answer;
}