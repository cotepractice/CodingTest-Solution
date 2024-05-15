#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int find(vector<int> &A, vector<int>& B,int minV){
    for(int i=minV;i>1;i--){
        bool f=false;
        for(auto a: A){
            if(a%i!=0){
                f=true;
                break;
            }
        }
        bool f2=false;
        if(!f){
            for(auto b: B){
                if(b%i==0){
                f2=true;
                break;
            }
            }
             if(!f2){ //f2는 
            return i;
        }
        }
        
       
    }
    return 0;
}
int solution(vector<int> arrayA, vector<int> arrayB) {
    int answer = 0;
    int minA=*min_element(arrayA.begin(),arrayA.end());
    int minB=*min_element(arrayB.begin(),arrayB.end());
    
     answer=max(find(arrayA, arrayB, minA),find(arrayB,arrayA, minB));
    return answer;
}