#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
 
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string num;
		cin >> num;
		string min_num = num;
		string max_num = num;

		for (int i = 0; i < num.length(); i++) {
			for (int j = i + 1; j < num.length(); j++) {
				if (i == 0 && num[j]=='0'){
					continue;
				}
				swap(num[i], num[j]);
				min_num = min(min_num, num);
				max_num = max(max_num, num);
				swap(num[j], num[i]);
			}
		}
		cout << "#" << t << " " << min_num << " " << max_num<<"\n";
	}
}