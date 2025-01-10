#include<iostream>
#include<stack>
using namespace std;

int T = 0;
int main() {
	int n;
	while (cin >> n)
	{
		T++;
		stack<char> stk;
		for(int i = 0; i < n; i++) {
			char c;
			cin >> c;
			if (c == '(' || c == '{' || c == '<' || c == '[')
			{
				stk.push(c);
			}
			else {
				bool f = false;
				if (!stk.empty()) {
					if ((stk.top() == '('&&c == ')') || (stk.top() == '{'&& c == '}') || (stk.top() == '<'&& c == '>') || (stk.top() == '['&& c == ']'))
					{
						stk.pop();
						continue;
					}
				}
				stk.push(c);
			}
			
			
		}

		if (stk.empty()) {
			cout <<"#"<<T<<" "<< 1<<endl;
		}
		else {
			cout <<"#"<<T<<" "<< 0<<endl;
		}
	}

}