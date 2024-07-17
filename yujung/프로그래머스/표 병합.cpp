#include <string>
#include <vector>
#include<sstream>
using namespace std;

int link[2501];
string value[2501];

int flatPos(int r, int c){
    return (r-1)*50+c;
}
vector<string> solution(vector<string> commands) {
    vector<string> answer;
  
    for(int i=1;i<=2500;i++){
        link[i]=i;
        value[i]="EMPTY";
    }
    stringstream ss;
    for(auto command: commands){
          vector<string> v;
        stringstream ss(command); // 이 형식에 주의. 까먹지 않기
        string tmp;
        while(ss>>tmp){v.push_back(tmp);}
        
        if(v[0]=="UPDATE"){
            if(v.size()==4){
                int pos=flatPos(stoi(v[1]),stoi(v[2]));
                string val=v[3];
                int parent=link[pos];
                value[parent]=val;
            }else{
                string val1=v[1],val2=v[2];
                for(int i=1;i<=2500;i++){
                    if(value[i]==val1)value[i]=val2;
                }
            }
        }else if(v[0]=="MERGE"){
            int pos1=flatPos(stoi(v[1]),stoi(v[2]));
            int pos2=flatPos(stoi(v[3]),stoi(v[4]));
            int parent1=link[pos1],parent2=link[pos2];
            if(parent1!=parent2){
                for(int i=1;i<=2500;i++){
                    if(link[i]==parent2)link[i]=parent1;
                }
                string val1=value[parent1],val2=value[parent2];
                if(val1=="EMPTY"&&val2!="EMPTY"){
                    value[parent1]=value[parent2];
                }else{
                    value[parent2]=value[parent1];
                }
            }
        }else if(v[0]=="UNMERGE"){
            int pos=flatPos(stoi(v[1]),stoi(v[2]));
            int parent=link[pos];
            string val=value[parent];
            for(int i=1;i<=2500;i++){
                if(link[i]==parent){
                    link[i]=i;
                    value[i]="EMPTY";
                }
            }
            value[pos]=val;
        }else{
            int pos=flatPos(stoi(v[1]),stoi(v[2]));
            int parent=link[pos];
            answer.push_back(value[parent]);
        }
        
    }
    return answer;
}