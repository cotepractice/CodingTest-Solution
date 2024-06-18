#include <string>
#include <vector>
#include<algorithm>
using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(),times.end());
    long long left=1;
    long long right=(long long)n*times.back(); //여기에 long long 타입 해주는게 매우 중요
    while(left<=right){
        long long mid=(left+right)/2;
        long long passed=0;
        for(auto t:times){
            passed+=mid/t;
        }
        if(passed>=n){
            right=mid-1;
            answer=mid;
        }else{
            left=mid+1;
        }
    }
    return answer;
}