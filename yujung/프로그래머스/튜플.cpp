#include <string>
#include <vector>
#include<algorithm>
#include<map>
//s가 표현하는 튜플의 원소는 1이상 100,00이하인 자연수
//return 하는 배열의 길이가 500이하인 경우

using namespace std;

map<int,int> m;
bool compare( pair<int, int> a,  pair<int, int> b) {
    return a.second > b.second; // value를 기준으로 내림차순 정렬
}
vector<int> solution(string s) {
    vector<int> answer;
  
    for(int i=2; i<s.size();i++){
        if(isdigit(s[i])){
            string a="";
            while(s[i]!=','&&s[i]!='}'){
                a+=(s[i]);
                i++;
            }
           m[stoi(a)]++;
        }
        
    }
    
    vector<pair<int,int>> v(m.begin(),m.end());
    sort(v.begin(), v.end(), compare);
      for (auto& p : v) {
        answer.push_back(p.first);
    }

    return answer;
}