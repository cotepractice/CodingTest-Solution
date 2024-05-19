#include <iostream>
using namespace std;


int solution(int n)
{
    int ans = 0;
    while(n!=0){
        int a=n%2;
        if(a==1){
            ans++;
        }
        n/=2;
    }
    

    return ans;
}