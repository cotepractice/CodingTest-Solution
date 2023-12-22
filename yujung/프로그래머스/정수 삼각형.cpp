#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int dp[500][500];

int solution(vector<vector<int>> triangle) {
    int answer = 0;
   // dp[0][0]=triangle[0][0];
    for(int i=1;i<triangle.size();i++){
        for(int j=0;j<=i;j++){
            if (j==0){
                triangle[i][j]=triangle[i-1][0]+triangle[i][j];
            }
            else if(j==i){
                triangle[i][j]=triangle[i-1][j-1]+triangle[i][j];
            }
            else{
               triangle[i][j]= max(triangle[i][j]+triangle[i-1][j-1], triangle[i][j]+triangle[i-1][j]);
            }
            answer=max(answer, triangle[i][j]);
        }
    }
    return answer;
}