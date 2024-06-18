#include <string>
#include <vector>

using namespace std;

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;
    for(int i=0; i<numbers.size();i++){
        if(numbers[i]%2==0){
            answer.push_back(numbers[i]+1);
        }else{
            long long bit=1;
            while(1){
                if((numbers[i]&bit)==0)break; //(numbers[i]&bit)를 해줘야함 비교연산자가 우선순위가 더 높음
                bit*=2;
            }
            bit=bit/2;
            answer.push_back(numbers[i]+bit);
        }
    }
    return answer;
}