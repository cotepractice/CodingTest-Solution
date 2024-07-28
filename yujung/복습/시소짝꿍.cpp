#include <string>
#include <vector>

using namespace std;

long long solution(vector<int> weights) {
    long long answer = 0;
    for(int i=0; i<weights.size();i++){
        for(int j=i+1; j<weights.size();j++){
            if(weights[i]==weights[j])answer++;
            if((weights[i]*2==weights[j]*3)||(weights[i]*3==weights[j]*2)){
                answer++;
            }
            if((weights[i]*2==weights[j]*4)||(weights[i]*4==weights[j]*2)){
                answer++;
            }
            if((weights[i]*4==weights[j]*3)||(weights[i]*3==weights[j]*4)){
                answer++;
            }
        }
    }
    return answer;
}