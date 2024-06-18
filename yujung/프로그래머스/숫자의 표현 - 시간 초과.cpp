#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;

    for(int k=2;k<=n;k++){
        for(int i=1;i<=n;i++){
        int sum=0;
        for(int j=i;j<i+k;j++){
            sum+=j;
            if(sum>n)break;
        }
        if(sum==n){answer++;}
    }
    }
    
    return answer;
}