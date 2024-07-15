#include <string>
#include <vector>

using namespace std;

string itob(long long num){
    string tmp="";
    while(num>0){
        tmp=to_string(num%2)+tmp;
        num/=2;
    }
    long long p=0;
    while(p<tmp.size()){
        p=p*2+1; 
    }
    while(p>tmp.size()){
        tmp="0"+tmp;
    }
    return tmp;
}

bool isAllZero(string tmp){
    for(int i=0; i<tmp.size();i++){
        if(tmp[i]!='0'){
            return false;
        }
    }
    return true;
}
bool dfs(string tmp){
    if(tmp.size()<=1||isAllZero(tmp)) return true;
    int mid=tmp.size()/2;
    string left=tmp.substr(0,mid);
    string right=tmp.substr(mid+1);
    return dfs(left)&&tmp[mid]=='1'&&dfs(right);
}
vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for(int i=0;i<numbers.size();i++){
        if(dfs(itob(numbers[i]))){
            answer.push_back(1);
        }else{
            answer.push_back(0);
        }
    }
    return answer;
}