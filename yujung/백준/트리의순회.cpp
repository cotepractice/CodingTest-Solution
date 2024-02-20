#include <iostream>
#include <vector>
using namespace std;
vector<int> inorder;
vector<int> postorder;
int Index[100001];
int N,root;
void preorder(int inStart, int inEnd, int postStart, int postEnd)
{
	if (inStart > inEnd || postStart > postEnd)
		return;

	int root = postorder[postEnd];
	int rootIndex = Index[root];
	int leftSize = rootIndex - inStart;


	cout << root << " ";

	preorder(inStart, rootIndex-1, postStart, postStart + leftSize-1);
	preorder(rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1);
}


int main(void)
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		inorder.push_back(num);
		Index[num] = i; // 중위 순회에서 num의 인덱스
	}
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		postorder.push_back(num);
	}
	preorder(0,N-1,0,N-1);

}