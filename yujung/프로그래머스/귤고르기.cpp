#include <string>
#include <vector>
#include<algorithm>
#include<map>
using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    map<int,int> m;
    for(auto a: tangerine){
        m[a]++;
    }
    vector<int> v;
    for(auto a:m){
        v. push_back(a.second);
    }
    sort(v.begin(),v.end());
    int tmp=tangerine.size()-k;
    int i=0;
    
    while(tmp!=0){
      if(tmp>=v[i]){ 
          tmp-=v[i];  
          v.erase(v.begin());
      }else{
          break;
      }
    }
    return v.size();
}