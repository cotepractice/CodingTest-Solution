#include <string>
#include <vector>

using namespace std;

int tmp[1001][1001];

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    for(int i=0; i<skill.size();i++){
        int n=skill[i][0];
        int x=skill[i][1];
        int y=skill[i][2];
        int ex=skill[i][3];
        int ey=skill[i][4];
        int num=skill[i][5];
        if(n==1)num*=-1;
         tmp[x][y]+=num;
         tmp[ex+1][y]-=num;
        tmp[x][ey+1]-=num;
        tmp[ex+1][ey+1]+=num;
    }
    
    
     //옆으로 누적합 
    for(int i=0;i<board.size();i++){
        for(int j=1; j<board[0].size();j++){
           tmp[i][j]+=tmp[i][j-1];
        }
    }
    
    //아래로 누적합
    for(int i=1;i<board.size();i++){
        for(int j=0; j<board[0].size();j++){
           tmp[i][j]+=tmp[i-1][j];
        }
    }
   
   for(int i=0;i<board.size();i++){
        for(int j=0; j<board[0].size();j++){
            if(board[i][j]+tmp[i][j]>0){
                answer++;
            }
        }
    }
    return answer;
}