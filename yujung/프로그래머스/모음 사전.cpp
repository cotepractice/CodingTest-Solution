#include <string>
#include <vector>

using namespace std;
string a="AEIOU";
int cnt=0;
int answer=0;
void dfs(string w,string word){
    //cnt++;
    if(w==word){answer=cnt;}
    if(w.size()>=5){return ;}
    for(int i=0; i<5;i++){
          cnt++;
    dfs(w+a[i],word);
    }
    
}
//단어 하나 word가 매개
int solution(string word) {
    dfs("",word);
    return answer;
  //     return answer-1;
}
