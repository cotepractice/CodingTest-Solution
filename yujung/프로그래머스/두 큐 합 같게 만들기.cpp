#include <string>
#include <vector>
#include<queue>
using namespace std;

//vector의 erase로 맨 앞 원소를 제하는 것은 시간복잡도가 O(n)으로 느림
int solution(vector<int> queue1, vector<int> queue2) {
 //원소의 값이 크고, 길이가 기므로 long long 필수
    long long sum=0;
    long long sum2=0;
    queue<int> q1;queue<int> q2;
  for(int i=0;i< queue1.size();i++){
      q1.push(queue1[i]);
      q2.push(queue2[i]);
      sum+=queue1[i];
      sum2+=queue2[i];
  }
    if((sum+sum2)%2==1)return -1;

    int cnt=0;
    int n=sum*3;
    
     while(n--){ 
        
         if(sum>sum2){
             int a=q1.front();
             q1.pop();
             sum-=a;
             q2.push(a);
             sum2+=a;
         }else if(sum<sum2){
              int a=q2.front();
         q2.pop();
         sum2-=a;
             q1.push(a);
             sum+=a;
         }else{
              return cnt;
         }
    cnt++;
  
     }
    return -1;
}