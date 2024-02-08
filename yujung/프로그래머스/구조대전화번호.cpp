#include <string>
#include <vector>
#include <map>
using namespace std;

bool solution(vector<string> phone_book)
{
    map<string,int> m;
    for(int i=0;i<phone_book.size();i++) m[phone_book[i]]++;//맵에 넣고
    for(int i=0;i<phone_book.size();i++)
        for(int j=1;j<phone_book[i].size();j++)
            if(m[phone_book[i].substr(0,j)]) return false;
	
    return true;
}