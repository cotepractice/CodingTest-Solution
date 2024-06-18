#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int total=brown+yellow; 

    int num=brown/2;//5
    int x;
    int y;
    for(int i=3; i<=num;i++){//2, 3, 
        int a=i;
        int b=num-a;
        //3 2

        if((a-2)*b==yellow){
            x=a;
            y=b+2;
           
        }
    }
     answer.push_back(x);
     answer.push_back(y);
    return answer;
}
