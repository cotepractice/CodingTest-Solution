#include <string>
#include <vector>
#include <iostream>
#include<map>
using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    int cnt =0;
    int f=1;
    map<string,int> m;
    m[words[0]]++;
    for(int i=0; i<words.size()-1;i++){
            cnt++;
        m[words[i+1]]++;
        if(words[i].back()!=words[i+1].front()){
            f=0;
            break;
        }
        if(m[words[i+1]]>=2){ 
             f=0;
            break;
        }
    
    }
    cnt++;
    int a;
    int b;
    if(cnt%n==0){
        a=cnt/n;
        b=n;
    }else{
        a=cnt/n+1; 
        b=cnt%n;
    }
    
    if(f){
        a=0;
        b=0;
    }
    answer.push_back(b);
    answer.push_back(a);
    return answer;
}