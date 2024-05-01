#include <iostream>
#include <list>
#include<iterator>
using namespace std;

int main(void)
{
    for(int t = 1; t <= 10; t++)
    {
        int n, x, y, s;
        char c;
        list<int> lt;
        
        cin >> n;
        for(int i = 0; i < n; i++)
        {
            cin >> x;
            lt.push_back(x);
        }
        
        cin >> n;
        for(int i = 0; i < n; i++)
        {
            list<int> tmp;
            auto itr = lt.begin();
            cin >> c >> x >> y;
            
           
            advance(itr, x);
            for(int j = 0; j < y; j++)
            {
                cin >> s;
                tmp.push_back(s);
            }
            lt.splice(itr, tmp);
        }
        
        cout << "#" << t << " ";
        auto itr = lt.begin();
        for(int i = 0; i < 10; i++, itr++)
            cout << *itr << " ";
        cout << endl;
    }
    
    return 0;
}