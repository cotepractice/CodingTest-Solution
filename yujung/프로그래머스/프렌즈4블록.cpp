#include <string>
#include <vector>
#include<set>
using namespace std;

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    //m 행, n열
    bool check=false;
   do {
       check=false;
    vector<pair<int,int>> v;
    for(int i=0; i<m-1;i++){
        for(int j=0; j<n-1;j++){
            if(board[i][j]=='0')continue;
          if(board[i][j]==board[i][j+1]&&board[i][j]==board[i+1][j+1]&&board[i][j]==board[i+1][j]){//같으면
               check=true;
               v.push_back({i,j});
          }
        }
    }
    
    for(auto a:v){
        int x=a.first;
        int y=a.second;
        for(int i=x;i<x+2;i++){
            for(int j=y;j<y+2;j++){
                if(board[i][j]!='0'){
                    answer++;
                      board[i][j]='0';
                }
              
            }
        }
    }
    
    for(int i=1; i<m;i++){
        for(int j=0; j<n;j++){
            if(board[i][j]=='0'){
                for(int k=i;k>0;k--){
                    if(board[k-1][j]=='0')break;
                    board[k][j]=board[k-1][j];
                    board[k-1][j]='0';
                }
            }
        }
    }
    }while(check==true);
    
    return answer;
}