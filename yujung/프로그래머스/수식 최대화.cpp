#include <string>
#include <vector>
#include<algorithm>
using namespace std;

char c[6][3]={{'*','+','-'},{'*','-','+'},{'-','*','+'},{'-','+','*'},{'+','*','-'},{'+','-','*'}};

long long cal(long long a, long long b, char c){
    if(c=='-')return a-b;
    else if(c=='+') return a+b;
    return a*b;
}
long long solution(string expression) {
    long long answer = 0;
    int n=expression.size();
    vector<long long> nums; //숫자는  long long 타입에 담고
    vector<char> operators; //연산자는 char에 담는게 핵심
    vector<char> oper={'+','-','*'};
     sort(oper.begin(), oper.end());
     string res;
    for(int i=0; i<n;i++){
       
        if(isdigit(expression[i])){
            res+=expression[i];
        }else{
            nums.push_back(stoll(res));
            operators.push_back(expression[i]);
            res="";
        }
    }
    
    nums.push_back(stoll(res));
    
   do{
       vector<long long> numTmp(nums);
       vector<char> operTmp(operators);
       for(int i=0; i<3;i++){
           for(int j=0; j<operTmp.size();){
               if(oper[i]==operTmp[j]){
                   long long res=cal(numTmp[j],numTmp[j+1],oper[i]);
                //    numTmp.erase(numTmp.begin()+j,numTmp.begin() + j + 2);
                    numTmp.erase(numTmp.begin()+j);
                    operTmp.erase(operTmp.begin()+j);
                     numTmp[j]= res;
               }else{
                   j++;
               }
           }
       }
       answer=max(answer,abs(numTmp[0]));
       
   }while(next_permutation(oper.begin(),oper.end()));
    return answer;
}