#include <string>
#include <vector>
//0시 
using namespace std;

vector<double> compute_degree(int second){ //시,분,초마다 움직이는 총 각도 합 계산
    //Tip h일 경우에 한시간 360도 중 30도를 돔, 분,시 순으로 움직이는 각도는 1/60배수로 줄어든다.
    int h=(second/3600);
    int m=(second%3600)/60;
    int s=(second%3600)%60;    
    double hdegree=(h%12)*30.0+m*(0.5)+s*(1/120.0);
    double mdegree=m*(6.0)+s*(0.1);
    double sdegree=s*(6.0);
    return vector<double>{hdegree, mdegree, sdegree};
}
//시간이랑 초 비교
bool cmp_hour(vector<double> a, vector<double> b){
    //0,1,2 순으로 시,분, 초
    if(a[0]>a[2]&&b[0]<=b[2])return true;
    if(a[2]==354&&a[0]>354)return true; //초 당 6도씩 움직이기 때문에 360으로 가는 경우가 아니라 354->0으로 건너띔
    return false;
}
//분이랑 초 비교
bool cmp_minute(vector<double> a, vector<double> b){
        if(a[1]>a[2]&&b[1]<=b[2])return true;
        if(a[2]==354&&a[1]>354)return true;
    return false;
}

int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
    int answer = 0;
    int start=h1*3600+m1*60+s1;
    int end=h2*3600+m2*60+s2;
    for(int i=start;i<end;i++){
        vector<double> v=compute_degree(i);
        vector<double> next_v=compute_degree(i+1);
        bool h=cmp_hour(v,next_v);
        bool m=cmp_minute(v,next_v);
        if(h&&m){
            if(next_v[0]==next_v[1]){answer+=1;}//정각일 경우, 3개당 동일
            else{answer+=2;}//분, 시 둘다 초와 겹칠 경우
        }else if(h||m){
            answer++; //한개만 겹칠 경우
        }
    }
    

    if(start==0||start==43200){answer++;} //처음 시작할때 0시 또는 12시에 시작할 수 있음
    return answer;
}