#include <iostream>
using namespace std;

template<class T>
class BST {
private:
	struct Node{
		T data;
		Node *left;
		Node *right;
	};
	Node *root;
	void printInorder(Node * ptr);
	void printPreorder(Node * ptr);
	void printPostorder(Node * ptr);
	T findLCA(Node *ptr,T x, T y);
	int find_minTurns(Node *ptr, T x, T y);

public:
	BST();
	~BST();
	void Inorder();
	void Preorder();
	void Postorder();
	bool Search(T x);
	void Insert(T x);
	void Delete(T x);
	T LCA(T x,T y);
	int minTurns(T x,T y);
};