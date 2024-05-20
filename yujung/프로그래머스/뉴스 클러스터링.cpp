#include <string>
#include<map>
using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    
    for(int i=0; i<str1.size();i++){
        str1[i]=tolower(str1[i]);
    }
    for(int i=0; i<str2.size();i++){
        str2[i]=tolower(str2[i]);
    }
    map<string,pair<int,int>> m;
    for(int i=0; i<str1.size()-1; i++)
        if(isalpha(str1[i]) && isalpha(str1[i+1]))
            m[str1.substr(i, 2)].first++; //영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버리는 것이 중요
    
    for(int i=0; i<str2.size()-1; i++)
        if(isalpha(str2[i]) && isalpha(str2[i+1]))
            m[str2.substr(i, 2)].second++;
    int sum=0;
    int inter=0;
    for(auto a: m){
        
        sum+=max(a.second.first,a.second.second);
        inter+=min(a.second.first,a.second.second);
    }
    double num;
    if(inter==0&&sum==0){
        num=1.0;
    }else{
        num=(double)inter/(double)sum;
    }
    
    answer=(num)*65536;
    
    return answer;
}