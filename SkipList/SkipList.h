#include <iostream>
using namespace std;

template<class T>
class SkipList {
public:
	SkipList();
	SkipList(int l);
	~SkipList();
	void Insert(T x);
	void Delete(T x);
	bool Search(T x);
	void Print();

private:
	struct Node {
		T data;
		Node* next[];
	};

	int max_level;
	float p;
	Node * head;
};