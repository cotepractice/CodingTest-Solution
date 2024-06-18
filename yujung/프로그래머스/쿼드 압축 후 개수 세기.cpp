#include <string>
#include <vector>
using namespace std;


int one=0;
int zero=0;

void recur(vector<vector<int>> & a,int x,int y, int size){//& 참조를 사용하는 경우에는 복사본 생성과 관련된 오버헤드가 없으므로 보통 더 빠름
    if(size==1){
        if (a[x][y] == 0) zero++;
        else one++;
       
        return;
    }
    
    bool f=true;
    int first=a[x][y];
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if(a[x+i][y+j]!=first){
               f=false;
            }
        }
        if(!f)break;
    }
  
    if(!f){
         recur(a,x,y,size/2);
  
     recur(a,x+size/2,y,size/2);
           recur(a,x,y+size/2,size/2);
     recur(a,x+size/2,y+size/2,size/2);
    }else{
        if (first == 0) zero++;
        else one++;
    }
        
     
  
   
}
vector<int> solution(vector<vector<int>> arr) {

    recur(arr,0,0, arr.size());
 	vector<int> answer = { zero, one };
    return answer;
}