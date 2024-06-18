#include <string>
#include <vector>

using namespace std;
bool visited[201];
  vector<int> answer;
vector<int> tmp;
int c;
void dfs(int cnt,int n,long long k){
    if(cnt==n){
        c++;
        if(c==k){
            answer=tmp;
        }
        return;
    }
    for(int i=1; i<=n;i++){
        if(visited[i]==true)continue;
        visited[i]=true;
        tmp.push_back(i);
       dfs(cnt+1,n,k); 
        visited[i]=false;
        tmp.pop_back();
    }
}
vector<int> solution(int n, long long k) {

     dfs(0, n,k);
    return answer;
}