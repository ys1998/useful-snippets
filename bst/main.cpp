#include <iostream>
#include "bst.cpp"
using namespace std;
int main(int argc, char const *argv[])
{
	char c='1';
	int a,x,y,n;
	BST<int> t;
	while(c!='0'){
		cin>>c;
		switch(c){
			case 'i':
			cin>>n;
			for(int i=0;i<n;++i){
				cin>>a; t.Insert(a);
			}
			break;
			case 'x':
			t.Inorder(); cout<<endl; break;
			case 'y':
			t.Preorder(); cout<<endl; break;
			case 'z':
			t.Postorder(); cout<<endl; break;
			case 's':
			cin>>a;
			cout<<(int)t.Search(a)<<endl; break;
			case 'd':
			cin>>a;
			t.Delete(a); break;
			case 'l':
			cin>>x>>y;
			cout<<t.LCA(x,y)<<endl; break;
			case 't':
			cin>>x>>y;
			cout<<t.minTurns(x,y)<<endl; break;
			default:
			break;
		}
	}
	return 0;
}