#include <string>
#include <vector>
//1행 1열부터 i행 i열까지 영역 내의 모든 빈칸을 숫자 i로 채웁니다.
//3,2,2,3
//4,3,3,3,4,4,4,4

using namespace std;

vector<int> solution(int n, long long left, long long right) {
     vector<int> answer;
     int a=left/n;//행
    int b=right/n;//행
    int a1=left%n;
    int b1=right%n;
    if(a==b){
         for(int j=a1;j<=b1;j++){
            int tmp=max(a+1,j+1);
            answer.push_back(tmp);
        }
    }
    else if(a==b+1){
        for(int j=a1;j<n;j++){
            int tmp=max(a+1,j+1);
            answer.push_back(tmp);
        }
         for(int j=0;j<=b1;j++){
            int tmp=max(b+1,j+1);
            answer.push_back(tmp);
        }
    }else{
        for(int j=a1;j<n;j++){
            int tmp=max(a+1,j+1);
            answer.push_back(tmp);
        }
        
         for(int i=a+1;i<=b-1;i++){
       for(int j=0;j<n;j++){
            int tmp=max(i+1,j+1);
            answer.push_back(tmp);
       }
             
    }
         for(int j=0;j<=b1;j++){
            int tmp=max(b+1,j+1);
            answer.push_back(tmp);
        }
    }
   
    
   
   

    return answer;
}