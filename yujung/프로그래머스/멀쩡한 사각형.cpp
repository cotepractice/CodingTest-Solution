using namespace std;

//유클리드 호제법
int gcd(int a, int b){
    if(a%b==0){
        return b;
    }
    return gcd(b,a%b);
}

long long solution(int w,int h) {
    long long answer = 1;
    int g;
    if(w>h){
        g=gcd(w,h);
    }else{
         g=gcd(h,w);
    }
    answer=(long long)w*h- (w/g+h/g-1)*g;
    return answer;
}