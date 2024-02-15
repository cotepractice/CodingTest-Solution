#include <string>
#include <vector>

using namespace std;
int first[5]={1,2,3,4,5};
int second[8]={2,1,2,3,2,4,2,5};
int third[10]={3,3,1,1,2,2,4,4,5,5};
int scores[3]={0,};
vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int n=answers.size();
    for(int i=0; i<answers.size();i++){
       
            if(first[i%5]==answers[i])scores[0]++;
      
            if(second[i%8]==answers[i])scores[1]++;
    
            if(third[i%10]==answers[i])scores[2]++;
      
    }
    int score=max(scores[0],max(scores[1],scores[2]));
    for(int i=0; i<3;i++){
        if(score==scores[i]){
            answer.push_back(i+1);
        }
    }
    return answer;
}