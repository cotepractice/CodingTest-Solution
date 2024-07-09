#include <string>
#include <vector>
#include<cmath>
using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    for(long long i=1;i<=r2;i++){
        int ry1=0;
        if(i<=r1){
            ry1=ceil(sqrt((((long long)r1*r1)-(i*i))));
        }
        int ry2=floor(sqrt((((long long)r2*r2)-(i*i))));
        answer+=(ry2-ry1+1);
    }
    answer*=4;
    return answer;
}