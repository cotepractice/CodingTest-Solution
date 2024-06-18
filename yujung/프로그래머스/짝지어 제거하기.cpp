#include <iostream>
#include<string>
#include<stack>
using namespace std;

int solution(string s)
{
    int answer = -1;
    stack<char> stk;
    for(int i=0; i<s.size();i++){
        if(stk.empty()||stk.top()!=s[i]){ //비어 있거나 s크기가 
            stk.push(s[i]);
        }else{
            stk.pop();
        }
    }
if(stk.empty())return 1;
    else return 0;

}