#include<iostream>
#include<queue>

#define max 100001
using namespace std;

priority_queue<int, vector<int>, less<int>> max_heap;
priority_queue<int, vector<int>, greater<int>> min_heap;

int arr[max];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n, val;
	cin >> n;
	while (n--) {
		cin >> val;
		if (max_heap.empty())
			max_heap.push(val);

		else if (max_heap.size() == min_heap.size())
			max_heap.push(val);
		else
			min_heap.push(val); 

		if (!max_heap.empty() && !min_heap.empty() && !(max_heap.top() <= min_heap.top()))
		{
			int a = max_heap.top();
			int b = min_heap.top();

			max_heap.pop();
			min_heap.pop();

			max_heap.push(b);
			min_heap.push(a);
		}
		if(!max_heap.empty()
		cout << max_heap.top()<<"\n";
	}
}