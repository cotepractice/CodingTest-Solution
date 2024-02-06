#include <string>
#include <vector>
#include<algorithm>

using namespace std;
int solution(vector<vector<int>> sizes) {
    int answer=0;
    int max_first=0;
    int max_second=0;
    for(int i=0;i<sizes.size();i++){
        if(sizes[i][0]<sizes[i][1]){
            swap(sizes[i][0],sizes[i][1]);
        }
        max_first=max(max_first,sizes[i][0]);
        max_second=max(max_second,sizes[i][1]);
    }
    return max_first*max_second;
}