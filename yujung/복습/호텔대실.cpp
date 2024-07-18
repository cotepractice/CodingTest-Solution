#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include<cstring>
using namespace std;

// 시간 문자열을 분으로 변환하는 함수
int h_to_m(int h, int m) {
    return h * 60 + m;
}

// 비교 함수 (end 시간을 기준으로 정렬하기 위해)
bool cmp(const vector<int>& a, const vector<int>& b) {
    return a[0] < b[0];
}

int solution(vector<vector<string>> book_time) {
    int n = book_time.size();
    vector<vector<int>> v(n);
    int minute[3601];
    memset(minute, 0, sizeof(minute));
    // 예약 시간을 분 단위로 변환
    for (int i = 0; i < n; ++i) {
        int start_h = stoi(book_time[i][0].substr(0, 2));
        int start_m = stoi(book_time[i][0].substr(3, 2));
        int end_h = stoi(book_time[i][1].substr(0, 2));
        int end_m = stoi(book_time[i][1].substr(3, 2));
        v[i].push_back(h_to_m(start_h, start_m));
        v[i].push_back(h_to_m(end_h, end_m));
        for(int j=v[i][0];j<v[i][1]+10;j++){
            minute[j]++;
        }
    }
    int res=0;
    for(int i=0; i<3601;i++){
        res=max(minute[i],res);
    }

    
    return res;
}
