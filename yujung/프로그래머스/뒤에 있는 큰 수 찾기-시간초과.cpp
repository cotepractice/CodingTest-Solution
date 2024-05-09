#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    bool f=false;
    for(int i=0; i<numbers.size()-1;i++){
        f=false;
        for(int j=i+1; j<numbers.size();j++){
            if(numbers[i]<numbers[j]){
                answer.push_back(numbers[j]);
                f=true;
                break;
            }
            
        }
        if(f==false){
                answer.push_back(-1);
            }
    
    }
    answer.push_back(-1);
    return answer;
}