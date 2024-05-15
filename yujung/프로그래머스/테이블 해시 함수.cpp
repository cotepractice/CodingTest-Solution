#include <string>
#include <vector>
#include<algorithm>
using namespace std;
int co;
bool cmp(vector<int> a,vector<int> b){

    if (a[co]==b[co]){ return a[0]>b[0]; }
    else{
            return a[co]<b[co];
    }
}
int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    int answer = 0;
    co=col-1;
   sort(data.begin(),data.end(),cmp);

    for(int i=row_begin;i<=row_end;i++){
          int sum=0;
        for(int j=0; j<data[0].size();j++){
            sum+=data[i-1][j]%i;
        }
        answer^=sum;
    }
      
  
return answer;
}