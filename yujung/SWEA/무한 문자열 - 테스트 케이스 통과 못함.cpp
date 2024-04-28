#include<iostream>
#include<string>
using namespace std;
//cabccabc  cabcab 이경우의 테스트 케이스를 생각하지 못함
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string a;
		string b;
		bool flag = false;
		cin >> a >> b;
		if (a.size() > b.size()) {
			for (int i = 0; i < a.size(); i++) {
				
				//cout << "i" << i << "a" << i % (b.size() + 1) << endl;
				if (a[i] != b[i % (b.size())])
				{

				//	cout << a[i] << b[i % (b.size())];
					flag = true;
					break;
				}

			}
		}
		else {
			for (int i = 0; i < b.size(); i++) {
				if (b[i] != a[i % (a.size())])
				{
					flag = true;
					break;
				}

			}
		}

		if (flag == true) {
			cout <<"#"<<t<<" "<<"no"<<"\n";
		}
		else {
			cout << "#" << t<< " " << "yes"<<"\n";
		}
	}
	
}