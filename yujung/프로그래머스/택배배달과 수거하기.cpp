#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    long long answer = 0;
    int p=0;
    int d=0;
    int cnt=0;
    for(int i=n-1;i>=0;i--){
        p-=deliveries[i];
        d-=pickups[i];
        while(1){
            if(p>=0&&d>=0){
                break;
            }
            p+=cap;
            d+=cap;
            cnt++;
        }
        answer+=(i+1)*2*cnt;
        cnt=0;
    }
    return answer;
}