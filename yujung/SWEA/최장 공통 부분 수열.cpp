#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


//int arr[1000+1][1000+1] 도 Stack 에 다 못들어가서 Runtime Error 가 남
//dp 배열은 전역변수로 선언해서 사용
using namespace std;
int arr[1001][1001];
int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;

	for (int tc = 1; tc <= t; tc++)
	{
		string a, b, ans = "";
	
		cin >> a >> b;

		if (a.size() > b.size())
			swap(a, b);

		for (int i = 1; i <= a.size(); i++)
		{
			for (int j = 1; j <= b.size(); j++)
			{
				if (a[i - 1] == b[j - 1])
					arr[i][j] = arr[i - 1][j - 1] + 1;
				else
					arr[i][j] = max(arr[i - 1][j], arr[i][j - 1]);
			}
		}
		cout << "#" << tc << " " << arr[a.size()][b.size()] << endl;
	}
	return 0;
}