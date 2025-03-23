#include<iostream>
#include<vector>
using namespace std;
// + ,-, * ,/
int n;
vector<int> v;
int max_v = -987654321;
int min_v = 987654321;
void dfs(int cnt  , int plus , int minus, int suply , int de, int sum)
{
	if (cnt == n-1) 
	{ 
		if (max_v < sum) 
		{
			max_v = sum;
		}
		if (min_v > sum)
		{
			min_v = sum;
		}

		return; 
	}

	if (plus > 0) 
	{
		dfs(cnt + 1, plus-1, minus, suply, de, sum +v[cnt+1] );
	}
	if (minus > 0)
	{
		dfs(cnt + 1, plus, minus-1, suply, de, sum - v[cnt + 1]);
	}
	if (suply > 0)
	{
		dfs(cnt + 1, plus, minus, suply-1, de, sum * v[cnt + 1]);
	}
	if (de > 0)
	{
		dfs(cnt + 1, plus, minus, suply, de-1, sum / v[cnt + 1]);
	}
}
int main() {
	
	int a, b, c, d;
	cin >> n;

	cin >> a >> b >> c >> d;
	for (int i = 0; i < n; i++)
	{
		int e;
		cin >> e;
		v.push_back(e);
	}

	dfs(0, a, b, c, d, v[0]);
	cout << max_v<<endl;
	cout << min_v;

}