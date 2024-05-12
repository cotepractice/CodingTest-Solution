#include <string>
#include <vector>
#include<cstring>
using namespace std;
//dp문제
int arr[1000001];
int solution(int x, int y, int n) {
    int answer = 0;
  //  memset(arr,1000001,sizeof(arr)); memset은 바이트 대상이므로 0또는 -1로 초기화할때만 사용
        for (int i = 1; i < 1000001; i++)
        arr[i] = 1000001;
    arr[y]=0;
    for(int i=y;i>x;i--){ // x와 y가 있음
        if(arr[i]!=1000001){ //arr[i]가 아니면, 
            if(i%3==0){ 
                arr[i/3]=min(arr[i/3],arr[i]+1);
            }
            if(i%2==0){
                arr[i/2]=min(arr[i/2],arr[i]+1);
            }
            if(i-n>0){
                arr[i-n]=min(arr[i-n],arr[i]+1);
            }
        }
    }
    if(arr[x]==1000001){
        return -1;
    }else{
          return arr[x];
    }
  
}