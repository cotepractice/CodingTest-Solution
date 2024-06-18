#include <string>
#include <vector>
#include<algorithm>
//튜브의 말해야 하는

using namespace std;

char arr[6]={'A','B','C','D','E','F'};
string deply(int num,int n){
    string s;
    while(num!=0){
        int a=num%n;
        if(a<10){
            s +=to_string(a);
        }else{
            s+=arr[a-10];
        }
        num/=n;
    }
    reverse(s.begin(),s.end());
    return s;
}

string func( int t,int n,int m,int p){
    string s="0";
    string ans;
    for(int i=1; i<t*m;i++){
        s+=deply(i,n);
    }
    int first=p-1;
    while(first<t*m){
        ans+=s[first];
        first+=m;
    }

    return ans;
}

string solution(int n, int t, int m, int p) {
    string answer = "";
    answer=func(  t, n, m, p);
    return answer;
}