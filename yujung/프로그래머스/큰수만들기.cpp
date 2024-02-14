#include <string>
#include <vector>

using namespace std;


string solution(string number, int k) {
    string answer = "";
    int num_size=number.size()-k;
    
    int first_num=0;
    
    for(int i=0; i< num_size;i++){
        int max_num=number[first_num];
        int max_idx=first_num;
        for(int j=first_num; j<=i+k;j++){
            if(max_num<number[j]){
                max_num=number[j];
                max_idx=j;
            }
        }
        answer+=max_num;
        first_num=max_idx+1;
    }
    
    return answer;
}