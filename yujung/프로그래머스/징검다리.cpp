#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    sort(rocks.begin(),rocks.end());
    int left=0;
    int right=distance;
    while(left<=right){
        int mid=(left+right)/2;
        int cnt=0;
        int prev=0;
        for(auto t:rocks){
            if(t-prev<mid){
                cnt++;
            }else{
                prev=t;
            }
        }
        if(distance-prev<mid)cnt++;
        if(cnt<=n){ //삭제된 징검다리 수가 실제 삭제되어야 할 개수보다 작은 경우, 거리의 최솟값을 늘려줌
            answer=max(answer,mid);
            left=mid+1;
        }else{
            right=mid-1;
        }
    }
    return answer;
}