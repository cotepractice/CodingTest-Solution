#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int n;
vector<int> team;
vector<vector<int>> teams;
void dfs(int cnt,int idx){
    if(n/2==cnt){
        teams.push_back(team);
    }
   for(int i=idx; i<n;i++){
       team.push_back(i);
       dfs(cnt+1,i+1);
       team.pop_back();
   }
}
void compute(int cnt,vector<int> team,vector<vector<int>> &dice,vector<int> & tmp ,int sum){
    if(cnt==n/2){
        tmp.push_back(sum);
        return;
    }
    for(int i=0; i<6;i++){
        sum+=dice[team[cnt]][i];
        compute(cnt+1,team, dice, tmp,sum);
        sum-=dice[team[cnt]][i];
    }
}
vector<int> solution(vector<vector<int>> dice) {
    vector<int> answer={0,0};
    n=dice.size();
    dfs(0,0);
    int start=0;
    int end=teams.size()-1;
    int max_v=0;
    while(start<end){
        vector<int> tmp1;
        vector<int> tmp2;
        compute(0, teams[start],dice, tmp1 ,0);
        compute(0, teams[end],dice, tmp2 ,0);
        sort(tmp1.begin(),tmp1.end());
        sort(tmp2.begin(),tmp2.end());
        
        int win1=0;
        int win2=0;
        for(auto n: tmp1){
            int a=lower_bound(tmp2.begin(),tmp2.end(),n)-tmp2.begin();
            if(a>0){
                win1+=a;
            }
        }
        
         for(auto n: tmp2){
            int a=lower_bound(tmp1.begin(),tmp1.end(),n)-tmp1.begin();
            if(a>0){
                win2+=a;
            }
        }
        if(win1>win2){
            if(win1>max_v){
                max_v=win1;
                answer=teams[start];
            }
        }else{
            if(win2>max_v){
                max_v=win2;
                answer=teams[end];
            }
        }
        tmp1.clear();
        tmp2.clear();
        start++;
        end--;
    }
    for(int i=0;i<answer.size();i++){
        answer[i]++;
    }
    return answer;
}