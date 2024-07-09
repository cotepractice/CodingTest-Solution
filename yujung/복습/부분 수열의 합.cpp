#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    int min_v=sequence.size();
    int n=sequence.size();
    int sum=0;
    answer.push_back(0);
    answer.push_back(0);
    for(int s=0, e=0;s<n;){
         
        
        if(k==sum&&min_v>(e-s)){
            answer[0]=s;
            answer[1]=e-1;
            min_v=e-s;
        }else if(sum<k&&e<n){
            sum+=sequence[e++];
        }else{
            sum-=sequence[s++];
        }
    }
    return answer;
}