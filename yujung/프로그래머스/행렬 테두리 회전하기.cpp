#include <string>
#include <vector>
#include<algorithm>
//시계방향으로 회전
//각 회전은 x1, y1,x2,y2인 정수 4개로 표현, 그 의미는 다음

//x1
using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<int> tmp;
    int arr[101][101];
    int num=0;
    for(int i=1;i<=rows;i++){
        for(int j=1; j<=columns;j++){
            num++;
            arr[i][j]=num;
        }
    }
    
    for(int i=0; i<queries.size();i++){
        int x1=queries[i][0];
         int y1=queries[i][1];
         int x2=queries[i][2];
         int y2=queries[i][3];
        for(int j=y1;j<y2;j++){
            tmp.push_back(arr[x1][j]);
        }
         for(int j=x1;j<x2;j++){
            tmp.push_back(arr[j][y2]);
        }
        for(int j=y2;j>y1;j--){
            tmp.push_back(arr[x2][j]);
        }
        for(int j=x2;j>x1;j--){
            tmp.push_back(arr[j][y1]);//
        }
    int res=*min_element(tmp.begin(),tmp.end());
       
        int t=tmp.back();
   
       tmp.erase(tmp.begin()+tmp.size()-1);
       tmp.insert(tmp.begin(),t);
        
    
 
        for(int j=y1;j<y2;j++){
             arr[x1][j]=tmp.front();
            tmp.erase(tmp.begin());
        }
         for(int j=x1;j<x2;j++){
              arr[j][y2]=tmp.front();
            tmp.erase(tmp.begin());
        }
        for(int j=y2;j>y1;j--){
             arr[x2][j]=tmp.front();
            tmp.erase(tmp.begin());
            
        }
        for(int j=x2;j>x1;j--){
         
              arr[j][y1]=tmp.front();
            tmp.erase(tmp.begin());
        }
      
      answer.push_back(res);
        tmp.clear();
    }

    return answer;
    
}