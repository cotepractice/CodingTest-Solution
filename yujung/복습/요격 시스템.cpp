#include <string>
#include <vector>
#include<algorithm>
using namespace std;

bool cmp(vector<int> a,vector<int> b){
    return a[1]<b[1];
}

int solution(vector<vector<int>> targets) {
    int answer = 0;
     sort(targets.begin(), targets.end(), cmp);
    
    
    int start=targets[0][0];
    int end=targets[0][1];
   
    int idx=1;
    int cnt=1;
    int max_v=-1;
    while(idx<targets.size()){
     int next_start=targets[idx][0];
    int next_end=targets[idx][1];
        
        
      if(end<=next_start){
          start=next_start;
          end=next_end;
          cnt++;
      }
      
      idx++;
    }
    return cnt;
}